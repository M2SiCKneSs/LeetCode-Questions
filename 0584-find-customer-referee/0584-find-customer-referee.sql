# Write your MySQL query statement below
SELECT c.name
FROM  Customer as c
WHERE NOT c.referee_id=2 OR c.referee_id is NULL