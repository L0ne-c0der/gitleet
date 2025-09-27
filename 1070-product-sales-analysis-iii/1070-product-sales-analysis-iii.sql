# Write your MySQL query statement below

#USing a Common Table Expression or CTE
#Write inner query first always

SELECT 
    t1.product_id,
    t2.first_year,
    t1.quantity,
    t1.price
FROM
    sales t1
JOIN
(
    SELECT 
        product_id,
        MIN(year) AS first_year 
    FROM
        sales
    GROUP BY
        product_id
) AS
    t2
ON
    t1.product_id = t2.product_id
    AND
    t2.first_year = t1.year
