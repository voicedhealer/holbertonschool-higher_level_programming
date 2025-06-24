-- Liste toutes les émissions de hbtn_0d_tvshows qui ont au moins un genre lié.
-- Le résultat est trié par titre d'émission et par ID de genre.

-- Sélectionne le titre de l'émission et l'ID du genre.
SELECT tv_shows.title, tv_show_genres.genre_id
-- Commence par la table tv_shows.
FROM tv_shows
-- La joint avec tv_show_genres car nous ne voulons que les émissions avec un genre.
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Trie d'abord par titre, puis par ID de genre.
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
