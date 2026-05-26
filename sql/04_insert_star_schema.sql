INSERT INTO dim_customers (customer_id, customer_unique_id, customer_city, customer_state)
SELECT DISTINCT customer_id, customer_unique_id, customer_city, customer_state
FROM stg_customers;

INSERT INTO dim_products (product_id, product_category_name, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
SELECT DISTINCT product_id, product_category_name, product_weight_g, product_length_cm, product_height_cm, product_width_cm
FROM stg_products;

INSERT INTO dim_date (date_key, full_date, year, month, day, quarter)
SELECT DISTINCT
    TO_CHAR(order_purchase_timestamp::DATE, 'YYYYMMDD')::INTEGER,
    order_purchase_timestamp::DATE,
    EXTRACT(YEAR FROM order_purchase_timestamp)::INTEGER,
    EXTRACT(MONTH FROM order_purchase_timestamp)::INTEGER,
    EXTRACT(DAY FROM order_purchase_timestamp)::INTEGER,
    EXTRACT(QUARTER FROM order_purchase_timestamp)::INTEGER
FROM stg_orders
WHERE order_purchase_timestamp IS NOT NULL;

INSERT INTO fact_orders (order_id, customer_key, product_key, date_key, order_status, total_revenue)
SELECT
    o.order_id,
    dc.customer_key,
    dp.product_key,
    dd.date_key,
    o.order_status,
    r.total_revenue
FROM stg_orders o
JOIN stg_customers c ON o.customer_id = c.customer_id
JOIN dim_customers dc ON c.customer_id = dc.customer_id
JOIN stg_order_revenue r ON o.order_id = r.order_id
LEFT JOIN stg_order_items oi ON o.order_id = oi.order_id
LEFT JOIN dim_products dp ON oi.product_id = dp.product_id
JOIN dim_date dd ON o.order_purchase_timestamp::DATE = dd.full_date;