-- Liste toutes les émissions du genre Comedy dans la base de données hbtn_0d_tvshows.

-- Sélectionne uniquement le titre de l'émission.
SELECT
    ts.title
-- Commence par la table des émissions.
FROM
    tv_shows AS ts
-- Jointure interne avec la table de liaison pour relier les émissions aux genres.
INNER JOIN
    tv_show_genres AS tsg ON ts.id = tsg.show_id
-- Jointure interne avec la table des genres pour filtrer par le nom du genre.
INNER JOIN
    tv_genres AS tg ON tsg.genre_id = tg.id
-- Filtre les résultats pour ne conserver que les émissions dont le genre est 'Comedy'.
WHERE
    tg.name = 'Comedy'
-- Trie les résultats par le titre de l'émission en ordre croissant.
ORDER BY
    ts.title ASC;
