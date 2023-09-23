-- Set up a MySQL server with the following configuration:
-- 1. Create the hbnb_test_db database if it doesn't exist.
-- 2. Create the hbnb_test user with the password hbnb_test_pwd, limited to localhost.
-- 3. Grant all privileges on the hbnb_test_db database to the hbnb_test user.
-- 4. Grant SELECT privilege on performance_schema to the hbnb_test user.
-- 5. Refresh privileges to apply the changes.

-- Step 1: Create the hbnb_test_db database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Step 2: Create the hbnb_test user with a secure password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Step 3: Grant all privileges on the hbnb_test_db database to the hbnb_test user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Step 4: Grant SELECT privilege on performance_schema to the hbnb_test user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Step 5: Refresh privileges to ensure the changes take effect
FLUSH PRIVILEGES;
