# Write your MySQL query statement below
SELECT 
    t2.name as Department, 
    t1.name as Employee,
    t1.salary as Salary
FROM 
    employee t1
JOIN
    department t2
ON
    t1.departmentId = t2.id
WHERE
    t1.salary =
(
    SELECT  MAX(salary) FROM employee 
    WHERE departmentId = t1.departmentId
)