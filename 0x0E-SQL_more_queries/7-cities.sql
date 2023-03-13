
-- CREATE database hbtn_0d_usa 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- CREATE a table cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT,
	name VARCHAR(256),
	FOREIGN KEY(state_id) REFERENCES states(id));

