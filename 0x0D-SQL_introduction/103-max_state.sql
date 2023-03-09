-- Display state and max temperature
SELECT state, MAX(value) AS 'max_temp'
ORDER BY state
