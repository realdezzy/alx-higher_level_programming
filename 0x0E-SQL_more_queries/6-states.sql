-- CREATE database hbtn_0d_usa 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- CREATE a table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256));
