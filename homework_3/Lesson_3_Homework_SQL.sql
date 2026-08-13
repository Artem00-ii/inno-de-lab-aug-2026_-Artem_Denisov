-- Lesson 3 Homework — SQL Practice
-- Required tasks only (Part 1–6)

-- SETUP
DROP TABLE IF EXISTS Shippings;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    country VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    item VARCHAR(50),
    amount INT,
    customer_id INT REFERENCES Customers(customer_id)
);

CREATE TABLE Shippings (
    shipping_id INT PRIMARY KEY,
    status VARCHAR(20),
    customer INT REFERENCES Customers(customer_id)
);

INSERT INTO Customers (customer_id, first_name, last_name, age, country) VALUES
(1, 'John', 'Doe', 31, 'USA'),
(2, 'Robert', 'Luna', 22, 'USA'),
(3, 'David', 'Robinson', 22, 'UK'),
(4, 'John', 'Reinhardt', 25, 'UK'),
(5, 'Betty', 'Doe', 28, 'UAE'),
(6, 'Alice', 'Smith', 35, 'USA'),
(7, 'Michael', 'Brown', 40, 'UK'),
(8, 'Sarah', 'Davis', 29, 'UAE'),
(9, 'Tom', 'White', 31, 'USA'),
(10, 'Emma', 'Green', 27, 'UK');

INSERT INTO Orders (order_id, item, amount, customer_id) VALUES
(1, 'Keyboard', 400, 4),
(2, 'Mouse', 300, 4),
(3, 'Monitor', 12000, 3),
(4, 'Keyboard', 400, 1),
(5, 'Mousepad', 250, 2),
(6, 'Monitor', 10000, 6),
(7, 'Keyboard', 450, 6),
(8, 'Mouse', 350, 7),
(9, 'Monitor', 11000, 9),
(10, 'Mousepad', 300, 10);

INSERT INTO Shippings (shipping_id, status, customer) VALUES
(1, 'Pending', 2),
(2, 'Pending', 4),
(3, 'Delivered', 3),
(4, 'Pending', 5),
(5, 'Delivered', 1),
(6, 'Delivered', 6),
(7, 'Pending', 7),
(8, 'Delivered', 9),
(9, 'Pending', 8),
(10, 'Delivered', 10);

-- PART 1: WHERE
-- Task 1
SELECT first_name, last_name, age, country
FROM Customers
WHERE country = 'USA' AND age > 25;

-- Task 2
SELECT order_id, item, amount, customer_id
FROM Orders
WHERE amount > 1000;

-- PART 2: JOIN
-- Task 1
SELECT c.first_name, c.last_name, o.item, o.amount
FROM Orders AS o
JOIN Customers AS c ON o.customer_id = c.customer_id;

-- Task 2
SELECT s.status, c.first_name, c.last_name
FROM Shippings AS s
JOIN Customers AS c ON s.customer = c.customer_id;

-- PART 3: GROUP BY
-- Task 1
SELECT country, COUNT(*) AS count
FROM Customers
GROUP BY country;

-- Task 2
SELECT item, COUNT(*) AS count, AVG(amount) AS avg_amount
FROM Orders
GROUP BY item;

-- PART 4: ORDER BY
-- Task 1
SELECT first_name, age
FROM Customers
ORDER BY age DESC;

-- PART 5: SUBQUERIES
-- Task 1
SELECT c.first_name, c.last_name, o.amount
FROM Customers AS c
JOIN Orders AS o ON c.customer_id = o.customer_id
WHERE o.amount = (SELECT MAX(amount) FROM Orders);

-- PART 6: WINDOW FUNCTIONS
-- Task 1
SELECT
    order_id,
    customer_id,
    item,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) AS total_by_customer
FROM Orders;
