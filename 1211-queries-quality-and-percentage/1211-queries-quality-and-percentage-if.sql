# Write your MySQL query statement below
#quality = AVG(rating/position) So, create a column rating/position ?
#poor qual % = (no of things less than 3 / total ) * 100

SELECT QUERY_NAME, ROUND(AVG(RATING/POSITION), 2) AS QUALITY, ROUND(AVG(IF(RATING<3,1,0))*100, 2) AS POOR_QUERY_PERCENTAGE
FROM QUERIES
GROUP BY QUERY_NAME