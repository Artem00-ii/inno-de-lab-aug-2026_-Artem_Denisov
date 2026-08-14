-- Part 1: WHERE
-- Task 2: Find all orders where amount is greater than 1000.

SELECT order_id, item, amount, customer_id
FROM Orders
WHERE amount > 1000;
