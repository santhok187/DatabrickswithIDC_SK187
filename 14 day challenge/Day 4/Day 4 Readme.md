# 🚀 Day 4 – Databricks 14 Days AI Challenge  
📅 12/01/26  
⚙️ Schema Governance & De‑duplication

---

## 📖 Learn
- What is Delta Lake?  
- ACID transactions  
- Schema enforcement  
- Delta vs Parquet  

---

## 🛠️ Tasks
1. Convert CSV to Delta format  
2. Create Delta tables (SQL and PySpark)  
3. Test schema enforcement  
4. Handle duplicate inserts  

---

## 🧑‍💻 Hands-On Work
- Converted October & November e‑commerce datasets from CSV to Delta format.  
- Created Delta tables using both SQL and PySpark APIs.  
- Demonstrated **schema enforcement** by attempting to append mismatched rows.  
- Applied **schema evolution** with `mergeSchema` to add new columns (`event_date`).  
- Built a duplicate events DataFrame and applied **MERGE (Upsert)** for idempotent ingestion.  

---

## 📊 Insights
- **Delta Lake** ensures reliability with ACID transactions.  
- Schema enforcement prevents bad data ingestion.  
- Schema evolution allows flexibility without breaking pipelines.  
- MERGE provides robust handling of duplicates and updates.  

---

## 🙌 Reflection
Day 4 highlighted the importance of **data governance** in modern data engineering.  
Delta Lake’s schema enforcement, evolution, and ACID guarantees make PySpark pipelines **scalable, reliable, and production‑ready**.

---

#DatabricksWithIDC #AIChallenge #PySpark #BigData #DataGovernance #DeltaLake #Day4