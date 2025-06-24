-- Crée la base de données hbtn_0d_usa et la table states.

-- Crée la base de données hbtn_0d_usa si elle n'existe pas déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Sélectionne la base de données hbtn_0d_usa pour les commandes suivantes.
USE hbtn_0d_usa;

-- Crée la table states si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
