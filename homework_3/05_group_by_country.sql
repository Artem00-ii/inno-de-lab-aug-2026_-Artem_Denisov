-- Part 3: GROUP BY
-- Task 1: Count the number of customers in each country.

SELECT country, COUNT(*) AS count
FROM Customers
GROUP BY country;
