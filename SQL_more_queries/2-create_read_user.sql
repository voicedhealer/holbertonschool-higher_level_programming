-- Crée la base de données hbtn_0d_2 et l'utilisateur user_0d_2.
-- L'utilisateur user_0d_2 doit avoir uniquement le privilège SELECT.

-- Crée la base de données hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorde le privilège SELECT à user_0d_2 sur la base hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applique les changements de privilèges.
FLUSH PRIVILEGES;
