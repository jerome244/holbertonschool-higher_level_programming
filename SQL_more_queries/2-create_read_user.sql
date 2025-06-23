-- 2-create_read_user.sql
-- Create database hbtn_0d_2 and user user_0d_2 with read-only access

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist and set password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload privilege tables to ensure changes take effect
FLUSH PRIVILEGES;
