-- Liste tous les genres de la base de données hbtn_0d_tvshows
-- et affiche le nombre d'émissions liées à chaque genre.
-- Seuls les genres avec au moins une émission sont affichés.
-- Le résultat est trié par le nombre d'émissions (décroissant).

-- Sélectionne le nom du genre et compte le nombre d'émissions pour ce genre.
SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
-- Part de la table des genres.
FROM
    tv_genres
-- Jointure interne avec la table de liaison genre-émission.
-- Une INNER JOIN garantit que seuls les genres liés à des émissions sont inclus.
INNER JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Regroupe les résultats par nom de genre pour que COUNT() s'applique à chaque groupe.
GROUP BY
    tv_genres.name
-- Trie les résultats par le nombre d'émissions en ordre décroissant.
ORDER BY
    number_of_shows DESC;
