-- Example SQL to create customer and transactions tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    country VARCHAR(50)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    transaction_date DATE,
    amount FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Example SQL to extract customer metrics (total spending, frequency, recency)
SELECT 
    c.customer_id, 
    c.name, 
    COUNT(t.transaction_id) AS total_purchases,
    SUM(t.amount) AS total_spent,
    MAX(t.transaction_date) AS last_purchase_date
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.name;
