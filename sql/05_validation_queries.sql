SELECT ROUND(SUM(total_revenue), 2) AS fact_total_revenue
FROM fact_orders;

SELECT ROUND(SUM(total_revenue), 2) AS processed_total_revenue
FROM stg_order_revenue;

SELECT COUNT(DISTINCT order_id) AS fact_order_count
FROM fact_orders;

SELECT COUNT(DISTINCT order_id) AS staging_order_count
FROM stg_orders;

SELECT customer_id, COUNT(*)
FROM dim_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT product_id, COUNT(*)
FROM dim_products
GROUP BY product_id
HAVING COUNT(*) > 1;

SELECT COUNT(*) AS missing_customer_keys
FROM fact_orders
WHERE customer_key IS NULL;

SELECT COUNT(*) AS missing_product_keys
FROM fact_orders
WHERE product_key IS NULL;

SELECT COUNT(*) AS missing_date_keys
FROM fact_orders
WHERE date_key IS NULL;