# Databricks notebook source
import dlt
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, LongType

schema = StructType([
    StructField("event_time", TimestampType(), True),
    StructField("event_type", StringType(), True),
    StructField("product_id", LongType(), True),
    StructField("category_id", LongType(), True),
    StructField("category_code", StringType(), True),
    StructField("brand", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("user_id", LongType(), True),
    StructField("user_session", StringType(), True)
])

source_dir = "/Volumes/workspace/ecommerce/ecommerce_data/Streaming/"

@dlt.table(
  comment="Bronze table: raw ecommerce events"
)
def bronze_events():
    return (spark.readStream.format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("header","true")
            .schema(schema)
            .load(source_dir)
            .withColumn("event_date", F.to_date("event_time"))
            .withColumnRenamed("user_session", "session_id"))

# COMMAND ----------

@dlt.table(
  comment="Silver table: cleaned and deduplicated events"
)
def silver_events():
    df = dlt.read_stream("bronze_events") \
        .filter(F.col("event_type").isin(["view", "cart", "purchased"])) \
        .filter(F.col("user_id").isNotNull()) \
        .filter(F.col("product_id").isNotNull()) \
        .filter(F.col("session_id").isNotNull()) \
        .withColumnRenamed("category_code", "category")

    return (df.withWatermark("event_time", "1 hour")
              .dropDuplicates(["user_id","session_id","event_time","event_type"]))

# COMMAND ----------

from pyspark.sql.window import Window

@dlt.table(
  comment="Gold: recent views per user"
)
def gold_user_recently_viewed():
    window = Window.partitionBy("user_id").orderBy(F.col("event_time").desc())
    df = dlt.read("silver_events").filter(F.col("event_type") == "view")
    return (df.withColumn("rn", F.row_number().over(window))
              .filter(F.col("rn") <= 20)
              .select("user_id","product_id","brand","category","price","event_time"))

# COMMAND ----------

@dlt.table(
  comment="Gold: products in user carts"
)
def gold_user_cart():
    return (dlt.read("silver_events")
            .filter(F.col("event_type") == "cart")
            .select("user_id","product_id","brand","category","price","event_time"))

# COMMAND ----------

@dlt.table(
  comment="Gold: top popular products"
)
def gold_product_popularity():
    return (dlt.read("silver_events")
            .groupBy("category","brand")
            .agg(F.countDistinct("product_id").alias("product_count"))
            .orderBy(F.col("product_count").desc())
            .limit(20))

# COMMAND ----------

@dlt.table(
  comment="Gold: co-view product pairs for recommendations"
)
def gold_coview_pairs():
    df = (dlt.read("silver_events")
          .filter(F.col("event_type") == "purchased")
          .select("session_id","product_id")
          .distinct())
    return (df.alias("p1")
            .join(df.alias("p2"), on="session_id")
            .filter(F.col("p1.product_id") < F.col("p2.product_id"))
            .select(F.col("p1.product_id").alias("product_id_1"),
                    F.col("p2.product_id").alias("product_id_2")))
