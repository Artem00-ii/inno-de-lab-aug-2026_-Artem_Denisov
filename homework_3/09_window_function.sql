-- Part 6: WINDOW FUNCTIONS
-- Task 1: For every order, show the total amount of all orders made by the same customer.

SELECT
    order_id,
    customer_id,
    item,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) AS total_by_customer
FROM Orders;
