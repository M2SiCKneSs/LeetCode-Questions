# Write your MySQL query statement below
SELECT name,unique_id
FROM Employees as E 
LEFT JOIN EmployeeUNI as U ON E.id = U.id
 