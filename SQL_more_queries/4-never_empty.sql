-- Crée la table id_not_null sur le serveur MySQL.
-- La colonne 'id' a une valeur par défaut de 1.

-- Crée la table id_not_null si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
