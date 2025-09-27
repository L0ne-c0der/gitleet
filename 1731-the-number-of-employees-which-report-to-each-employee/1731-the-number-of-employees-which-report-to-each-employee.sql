# Write your MySQL query statement below
SELECT 
    E.employee_id,
    E.name,
    E.Managers.reports_count,
    Managers.average_age 
FROM
    Employees E
RIGHT JOIN
    (
        SELECT 
            reports_to,
            COUNT(reports_to) AS reports_count,
            ROUND(AVG(age),0) as average_age
        FROM
            employees
        WHERE
            reports_to IS NOT NULL
        GROUP BY
            reports_to
    ) AS Managers
ON
    E.employee_id = Managers.reports_to
