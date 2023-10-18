-- creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows.

-- use database hbtn_0c_0
USE hbtn_0c_0;
-- create table second_table if it doesn't exist and add columns
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- insert Rows into table second_table
INSERT INTO second_table (id, name, score)
VALUES ROW(1, 'John', 10), ROW(2, 'Alex', 3), ROW(3, 'Bob', 14), ROW(4, 'George', 8);
