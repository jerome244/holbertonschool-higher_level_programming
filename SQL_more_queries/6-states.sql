-- 6-states.sql
-- Create database hbtn_0d_usa and table states with id INT AUTO_INCREMENT PRIMARY KEY and name VARCHAR(256) NOT NULL

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
