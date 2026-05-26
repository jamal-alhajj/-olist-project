Customers
- Primary key: customer_id
- Missing values: none (all 5 columns have 0 missing values)
- Relationship: linked to orders via customer_id

Orders
- Primary key: order_id
- Foreign key: customer_id
- Issues / Missing values:

     order_approved_at: 160 missing
     order_delivered_carrier_date: 1783 missing
     order_delivered_customer_date: 2965 missing


