CREATE MATERIALIZED VIEW workspace.ecommerce.ecom_bronze_events AS
SELECT
    CAST(data.user_id        AS STRING)   AS user_id,
    CAST(data.user_session   AS STRING)   AS session_id,
    CAST(data.event_time     AS TIMESTAMP)AS event_time,
    CAST(data.event_type     AS STRING)   AS event_type,
    CAST(data.product_id     AS BIGINT)   AS product_id,
    CAST(data.brand          AS STRING)   AS brand,
    CAST(data.category_code  AS STRING)   AS category,
    CAST(data.price          AS DOUBLE)   AS price,
    TO_DATE(data.event_time)              AS event_date
FROM read_files(
    '/Volumes/workspace/ecommerce/ecommerce_data/Batch/',
    format => 'csv',
    header => 'true'
) AS data;