-- Count rows and order by descending order
SELECT score, COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC
