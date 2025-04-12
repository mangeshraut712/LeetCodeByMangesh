SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status LIKE 'cancelled_%' THEN 1 ELSE 0 END) 
        / 
        COUNT(t.id)
    , 2) AS `Cancellation Rate`
FROM 
    Trips t
JOIN 
    Users uc ON t.client_id = uc.users_id AND uc.banned = 'No'
JOIN 
    Users ud ON t.driver_id = ud.users_id AND ud.banned = 'No'
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.request_at
ORDER BY
    Day;
