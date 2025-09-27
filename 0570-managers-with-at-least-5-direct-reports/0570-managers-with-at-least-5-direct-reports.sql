# Write your MySQL query statement below
SELECT
    name
FROM
    Employee
JOIN
    (
        SELECT 
            managerId
        FROM
            EMPLOYEE
        GROUP BY
            managerId
        HAVING
            COUNT(managerId) >= 5
    ) AS Managers
ON
    Employee.id = Managers.managerId