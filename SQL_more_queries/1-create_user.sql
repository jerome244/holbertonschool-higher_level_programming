-- 1-create_user.sql
-- Create MySQL user user_0d_1 with all privileges on the server

-- Create user if it does not exist and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reload privilege tables to ensure changes take effect
FLUSH PRIVILEGES;
