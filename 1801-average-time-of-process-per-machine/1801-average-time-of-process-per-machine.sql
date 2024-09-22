# Write your MySQL query statement below
SELECT machine_id , ROUND(SUM(sub)/COUNT(process_id ),3) AS processing_time 
FROM(
SELECT A1.machine_id,A1.process_id,A3.timestamp-A1.timestamp AS sub
FROM 
(
    SELECT machine_id , process_id , activity_type , timestamp 
    FROM Activity 
    WHERE activity_type = 'start'
) AS A1
JOIN (
    SELECT A2.machine_id , A2.process_id , A2.activity_type , A2.timestamp 
    FROM Activity A2
    WHERE A2.activity_type = 'end'
) AS A3
ON A1.machine_id = A3.machine_id AND A1.process_id = A3.process_id) AS A4
GROUP BY machine_id


