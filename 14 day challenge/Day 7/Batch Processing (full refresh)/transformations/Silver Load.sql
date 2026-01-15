CREATE MATERIALIZED VIEW workspace.ecommerce.ecom_silver_events AS
SELECT *
FROM (
    SELECT *, row_number() OVER (PARTITION BY user_id, session_id, event_time, event_type ORDER BY product_id) AS rn
    FROM workspace.ecommerce.ecom_bronze_events
    WHERE event_type IN ('view', 'cart', 'purchased')
      AND user_id IS NOT NULL
      AND session_id IS NOT NULL
      AND product_id IS NOT NULL
) sub
WHERE rn = 1;