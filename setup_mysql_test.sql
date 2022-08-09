-- Create a new DataBase 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a new USER and SET PASSWORD 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Giving all previleges to user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Giving SELECT previleges to user 'hbnbn_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
