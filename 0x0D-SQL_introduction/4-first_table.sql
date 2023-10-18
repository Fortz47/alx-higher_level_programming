-- creates a table called first_table in the current database
-- in your MySQL server

-- use database hbtn_0c_0
USE hbtn_0c_0;
-- create table if it doesn't exist and add fields
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
	);
