-- Liste toutes les émissions et tous les genres liés à ces émissions
-- depuis la base de données hbtn_0d_tvshows.
-- Si une émission n'a pas de genre, affiche NULL dans la colonne du genre.
-- Les résultats sont triés par titre d'émission et nom de genre.

-- Sélectionne le titre de l'émission et le nom du genre.
SELECT
    s.title,
    g.name
-- Commence par la table tv_shows (alias 's'), car nous voulons toutes les émissions.
FROM
    tv_shows AS s
-- Jointure gauche avec la table de liaison tv_show_genres (alias 'sg')
-- pour inclure toutes les émissions, même celles sans genre.
LEFT JOIN
    tv_show_genres AS sg ON s.id = sg.show_id
-- Jointure gauche avec la table tv_genres (alias 'g') pour obtenir le nom du genre.
-- Une LEFT JOIN est utilisée ici aussi pour propager le NULL si sg.genre_id est NULL.
LEFT JOIN
    tv_genres AS g ON sg.genre_id = g.id
-- Trie les résultats d'abord par le titre de l'émission, puis par le nom du genre.
ORDER BY
    s.title ASC,
    g.name ASC;
