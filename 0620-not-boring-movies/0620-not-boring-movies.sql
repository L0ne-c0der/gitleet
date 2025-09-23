# Write your MySQL query statement below
SELECT * FROM cinema
WHERE
id%2 != 0 
AND
description not like "%boring%"
ORDER BY rating DESC;