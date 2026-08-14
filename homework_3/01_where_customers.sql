-- Part 1: WHERE
-- Task 1: Find all customers from USA who are older than 25.

SELECT first_name, last_name, age, country
FROM Customers
WHERE country = 'USA' AND age > 25;
