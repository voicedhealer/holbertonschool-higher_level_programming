-- Liste toutes les émissions de hbtn_0d_tvshows et leurs IDs de genre.
-- Si une émission n'a pas de genre, affiche NULL pour l'ID du genre.
-- Le résultat est trié par titre d'émission et par ID de genre.

-- Sélectionne le titre de l'émission et l'ID du genre.
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
-- Commence par la table tv_shows, notre table "principale".
FROM
    tv_shows
-- Jointure gauche avec tv_show_genres pour inclure toutes les émissions,
-- même celles sans genre.
LEFT JOIN
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Trie d'abord par titre de l'émission, puis par ID du genre.
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
