# Write your MySQL query statement below
SELECT customer_id ,COUNT(customer_id) as count_no_trans 
FROM Visits as V LEFT JOIN Transactions as T ON V.visit_id=T.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id 

