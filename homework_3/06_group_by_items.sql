-- Part 3: GROUP BY
-- Task 2: Count orders and calculate the average amount for each item.

SELECT item, COUNT(*) AS count, AVG(amount) AS avg_amount
FROM Orders
GROUP BY item;
