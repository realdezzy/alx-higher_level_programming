--List top three
SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY AVG(value) DESC
LIMIT 3
