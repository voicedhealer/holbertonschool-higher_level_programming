-- Crée la table force_name sur le serveur MySQL.
-- La colonne 'name' ne peut pas être nulle.

-- Crée la table force_name si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
