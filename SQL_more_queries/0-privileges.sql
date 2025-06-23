-- Ce script liste tous les privilèges des utilisateurs MySQL
-- user_0d_1 et user_0d_2 sur le serveur.

-- Affiche les privilèges pour l'utilisateur user_0d_1.
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Affiche les privilèges pour l'utilisateur user_0d_2.
SHOW GRANTS FOR 'user_0d_2'@'localhost';
