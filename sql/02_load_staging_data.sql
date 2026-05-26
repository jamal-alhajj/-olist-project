COPY stg_customers
FROM 'C:/olist-project/data/clean/customers_clean.csv'
DELIMITER ','
CSV HEADER;

COPY stg_products
FROM 'C:/olist-project/data/clean/products_clean.csv'
DELIMITER ','
CSV HEADER;

COPY stg_orders
FROM 'C:/olist-project/data/clean/orders_clean.csv'
DELIMITER ','
CSV HEADER;

COPY stg_order_revenue
FROM 'C:/olist-project/data/enriched/orders_revenue.csv'
DELIMITER ','
CSV HEADER;

COPY stg_order_items
FROM 'C:/olist-project/data/clean/order_items_clean.csv'
DELIMITER ','
CSV HEADER;