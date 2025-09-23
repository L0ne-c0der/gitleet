# Write your MySQL query statement below
SELECT w2.id
FROM weather w2
JOIN weather w1
ON DATEDIFF(w2.recordDate,w1.recordDate) = 1
WHERE
w2.temperature > w1.temperature