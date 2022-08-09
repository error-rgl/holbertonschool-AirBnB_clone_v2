-- Creating the new DataBase hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating a new USER and SET PASSWORD 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- giving all privileges to user 'hbnb_dev' in the db 'hbnb_dev_db'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- giving SELECT privileges to user 'hbnb_dev' in the db 'performance_schema'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
--

