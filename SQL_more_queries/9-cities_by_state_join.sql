-- Liste toutes les villes contenues dans la base hbtn_0d_usa.
-- Chaque enregistrement affiche : cities.id, cities.name, states.name.

-- Sélectionne les colonnes requises depuis les deux tables.
SELECT cities.id, cities.name, states.name
-- Commence par la table 'cities' et la joint avec 'states'.
FROM cities
-- La jointure se fait sur la condition que state_id de cities correspond à l'id de states.
INNER JOIN states ON cities.state_id = states.id
-- Trie le résultat final par l'id des villes.
ORDER BY cities.id ASC;
