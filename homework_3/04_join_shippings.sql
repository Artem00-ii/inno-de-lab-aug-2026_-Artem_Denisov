-- Part 2: JOIN
-- Task 2: Show shipping status together with the customer's name.

SELECT s.status, c.first_name, c.last_name
FROM Shippings AS s
JOIN Customers AS c ON s.customer = c.customer_id;
