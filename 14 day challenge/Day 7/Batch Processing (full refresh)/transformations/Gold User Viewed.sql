CREATE MATERIALIZED VIEW workspace.ecommerce.ecom_gold_user_viewed AS
WITH viewed AS (
  SELECT
    user_id, product_id, brand, category, price, event_time,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_time DESC) AS rn
  FROM ecommerce.ecom_silver_events
  WHERE event_type = 'view'
)
SELECT user_id, product_id, brand, category, price, event_time
FROM viewed
WHERE rn <= 20;