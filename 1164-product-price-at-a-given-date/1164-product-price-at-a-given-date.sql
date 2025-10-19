# Write your MySQL query statement below
#i think we need to use correlated query
#we need to find the latest dates for a product_id less than or equal to current date
#union with
#product id that has no such date, to which we assign 10 as the price for that product, as it is the init value

WITH before_products AS
(
    SELECT product_id, MAX(change_date) as change_date
    FROM products
    WHERE DATEDIFF(change_date,'2019-08-16') <= 0
    GROUP BY product_id
)

SELECT t1.product_id, t1.new_price AS price
FROM products t1
INNER JOIN before_products t2
ON 
t1.product_id = t2.product_id
AND 
t1.change_date = t2.change_date

UNION ALL

SELECT product_id, (10) AS price
FROM products
GROUP BY product_id
HAVING DATEDIFF(MIN(change_date), '2019-08-16') > 0;