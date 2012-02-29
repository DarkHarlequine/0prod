mysql -u root -p
CREATE DATABASE IF NOT EXISTS 0_prod;
CREATE USER 'user0'@'localhost' IDENTIFIED BY 'test623';
use 0_prod;
GRANT ALL ON O_prod.* TO 'user0'@'localhost';
quit
