-- 5-unique_id.sql
-- Create table unique_id with id INT NOT NULL DEFAULT 1 and UNIQUE constraint, and name VARCHAR(256)
-- The database name will be passed as an argument to the mysql command

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
