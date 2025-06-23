-- 3-force_name.sql
-- Create table force_name with id INT and name VARCHAR(256) NOT NULL
-- The database name will be passed as an argument to the mysql command

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
