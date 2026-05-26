CREATE TABLE dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id TEXT UNIQUE,
    customer_unique_id TEXT,
    customer_city TEXT,
    customer_state TEXT
);

CREATE TABLE dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id TEXT UNIQUE,
    product_category_name TEXT,
    product_weight_g NUMERIC,
    product_length_cm NUMERIC,
    product_height_cm NUMERIC,
    product_width_cm NUMERIC
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_orders (
    fact_order_key SERIAL PRIMARY KEY,
    order_id TEXT,
    customer_key INTEGER REFERENCES dim_customers(customer_key),
    product_key INTEGER REFERENCES dim_products(product_key),
    date_key INTEGER REFERENCES dim_date(date_key),
    order_status TEXT,
    total_revenue NUMERIC
);