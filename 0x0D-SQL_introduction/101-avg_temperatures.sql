-- Display average temperature
SELECT city, AVG(value) AS 'avg_temp'
FROM temperature
ORDER BY value DESC
