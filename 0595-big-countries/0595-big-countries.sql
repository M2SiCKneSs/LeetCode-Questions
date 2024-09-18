# Write your MySQL query statement below
SELECT w.name,w.area,w.population 
FROM World as w
WHERE w.area>=3000000  OR  w.population>=25000000
