-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Alter Database
ALTER DATABASE hbtn_0c_0
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_unicode_ci;

-- Alter table
ALTER TABLE hbtn_0c_0.first_table
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter field
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256)  COLLATE utf8mb4_unicode_ci;;
