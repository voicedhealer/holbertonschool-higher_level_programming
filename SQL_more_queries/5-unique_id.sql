-- Crée la table unique_id sur le serveur MySQL.
-- La colonne 'id' a une valeur par défaut de 1 et doit être unique.

-- Crée la table unique_id si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
