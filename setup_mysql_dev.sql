-- Set up MySQL server with the following steps:
-- 1. Create the hbnb_dev_db database if it doesn't exist.
-- 2. Create the hbnb_dev user with the password hbnb_dev_pwd, restricted to localhost.
-- 3. Grant all privileges on hbnb_dev_db to the hbnb_dev user.
-- 4. Grant SELECT privilege on performance_schema to the hbnb_dev user.
-- 5. Refresh privileges to apply the changes.

-- Step 1: Create the hbnb_dev_db database if not already existent
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Step 2: Create the hbnb_dev user with a secure password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Step 3: Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Step 4: Grant SELECT privilege on performance_schema to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Step 5: Refresh privileges to apply the changes
FLUSH PRIVILEGES;
