-- 7-cities.sql
-- Create database hbtn_0d_usa and table cities with id INT AUTO_INCREMENT PRIMARY KEY,
-- state_id INT NOT NULL referencing states(id), and name VARCHAR(256) NOT NULL

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create cities table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
