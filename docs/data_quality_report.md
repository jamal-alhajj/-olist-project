Data Quality Report
Customers

Primary key: customer_id

Missing values: none

Relationship: linked to orders

Missing values per column:

customer_id                 0
customer_unique_id          0
customer_zip_code_prefix    0
customer_city               0
customer_state              0


Observations:

All 99,441 customers have complete information.

No cleaning required for missing values.

Orders

Primary key: order_id

Foreign key: customer_id

Issues: missing delivery dates (order_delivered_carrier_date and order_delivered_customer_date)

Missing values per column:

order_id                            0
customer_id                         0
order_status                        0
order_purchase_timestamp            0
order_approved_at                 160
order_delivered_carrier_date     1783
order_delivered_customer_date    2965
order_estimated_delivery_date       0


Observations:

Missing values are mainly in delivery and approval dates.

Can affect calculations for delivery time and revenue analysis.

Order Items

Primary key: combination of order_id + order_item_id

Foreign keys: order_id, product_id, seller_id

Missing values: none

Missing values per column:

order_id               0
order_item_id          0
product_id             0
seller_id              0
shipping_limit_date    0
price                  0
freight_value          0


Observations:

All 112,650 order items have complete data.

Products

Primary key: product_id

Missing values: some in category, name, description, photos, and dimensions

Missing values per column:

product_id                      0
product_category_name         610
product_name_lenght           610
product_description_lenght    610
product_photos_qty            610
product_weight_g                2
product_length_cm               2
product_height_cm               2
product_width_cm                2


Observations:

Missing values in non-critical fields (like product description or dimensions)

Small proportion of dataset (610/32,951 ≈ 1.85%)

Can impute or drop these records depending on analysis