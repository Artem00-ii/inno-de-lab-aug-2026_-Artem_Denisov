-- Part 2: JOIN
-- Task 1: Show orders together with the name of the customer.

SELECT c.first_name, c.last_name, o.item, o.amount
FROM Orders AS o
JOIN Customers AS c ON o.customer_id = c.customer_id;
