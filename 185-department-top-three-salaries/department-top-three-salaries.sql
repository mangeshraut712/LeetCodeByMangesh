WITH RankedSalaries AS (
    SELECT
        e.name AS EmployeeName,
        e.salary,
        e.departmentId,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as salary_rank
    FROM
        Employee e
)
SELECT
    d.name AS Department,
    rs.EmployeeName AS Employee,
    rs.salary AS Salary
FROM
    RankedSalaries rs
JOIN
    Department d ON rs.departmentId = d.id
WHERE
    rs.salary_rank <= 3;
