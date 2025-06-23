-- Crée l'utilisateur MySQL user_0d_1 et lui accorde tous les privilèges.

-- Crée l'utilisateur 'user_0d_1' avec le mot de passe 'user_0d_1_pwd',
-- seulement s'il n'existe pas déjà pour éviter les erreurs.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde tous les privilèges sur toutes les bases de données et toutes les tables
-- à l'utilisateur 'user_0d_1'.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applique les changements de privilèges pour qu'ils soient effectifs immédiatement.
FLUSH PRIVILEGES;
