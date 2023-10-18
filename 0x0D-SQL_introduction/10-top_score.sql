-- lists all records of the table second_table of the
-- database hbtn_0c_0 in your MySQL server.

-- use database hbtn_0c_0
USE hbtn_0c_0;
-- lists all records of table_second in order of greater score value
SELECT score, name FROM second_table ORDER BY score DESC;
