-- Liste tous les genres de l'émission "Dexter" de la base de données hbtn_0d_tvshows.

-- Sélectionne uniquement le nom du genre.
SELECT
    tg.name
-- Commence par la table des genres.
FROM
    tv_genres AS tg
-- Jointure interne avec la table de liaison pour trouver les correspondances entre genres et émissions.
INNER JOIN
    tv_show_genres AS tsg ON tg.id = tsg.genre_id
-- Jointure interne avec la table des émissions pour filtrer par le titre de l'émission.
INNER JOIN
    tv_shows AS ts ON tsg.show_id = ts.id
-- Filtre les résultats pour ne conserver que les genres associés à l'émission "Dexter".
WHERE
    ts.title = 'Dexter'
-- Trie les résultats par le nom du genre en ordre croissant.
ORDER BY
    tg.name ASC;
