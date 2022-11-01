-- converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0;
ALTER DATABASE
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256);
