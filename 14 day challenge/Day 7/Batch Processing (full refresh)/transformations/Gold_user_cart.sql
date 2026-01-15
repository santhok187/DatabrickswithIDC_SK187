CREATE MATERIALIZED VIEW workspace.ecommerce.ecom_gold_user_cart AS
  SELECT
    user_id, product_id, brand, category, price, event_time
  FROM ecommerce.ecom_silver_events
  WHERE event_type = 'cart'
  ORDER BY event_time DESC