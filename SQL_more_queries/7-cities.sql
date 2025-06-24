-- Crée la base de données hbtn_0d_usa et la table cities.

-- Crée la base de données hbtn_0d_usa si elle n'existe pas déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données hbtn_0d_usa pour les commandes suivantes.
USE hbtn_0d_usa;

-- Crée la table cities si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
