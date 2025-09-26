# Write your MySQL query statement below
#quality = AVG(rating/position) So, create a column rating/position ?
#poor qual % = (no of things less than 3 / total ) * 100

SELECT query_name , 
    ROUND((AVG(rating/position)),2) AS quality,
    ROUND(
        (SELECT COUNT(rating) FROM Queries t2
        WHERE 
            t2.query_name = t1.query_name
            AND t2.rating<3
        ) * 100
        / COUNT(rating)
    ,2) AS poor_query_percentage
FROM
    Queries t1
GROUP BY query_name;