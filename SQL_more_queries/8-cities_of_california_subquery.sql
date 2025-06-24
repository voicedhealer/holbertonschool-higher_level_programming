-- Liste toutes les villes de Californie trouvées dans la base de données hbtn_0d_usa.
-- Le résultat est trié par l'ID des villes.

-- Sélectionne l'ID et le nom des villes.
SELECT id, name
-- Depuis la table des villes.
FROM cities
-- Où l'ID de l'état correspond à l'ID de la Californie (trouvé via une sous-requête).
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
-- Trie les résultats par l'ID de la ville en ordre croissant.
ORDER BY id ASC;
