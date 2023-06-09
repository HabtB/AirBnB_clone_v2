-- this script prepares a MySQL server for the project
-- Create the database hbnb_dev_db (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user hbnb_dev (if it doesn't already exist)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to ensure that the new permissions are loaded
FLUSH PRIVILEGES;

-- Exit the MySQL prompt
exit
