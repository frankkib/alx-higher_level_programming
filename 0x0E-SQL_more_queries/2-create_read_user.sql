--A  script that creates the MySQL server user user_0d_1.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2pwd';
GRANT SELECT ON hbtn_0d_.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
