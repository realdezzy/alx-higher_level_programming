-- Get list of cities in california
SELECT * FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'Carlifornia')
ORDER BY cities.id ASC;
