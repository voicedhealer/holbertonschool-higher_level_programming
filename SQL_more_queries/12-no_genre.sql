-- Liste toutes les émissions de hbtn_0d_tvshows qui n'ont pas de genre lié.
-- Le résultat est trié par titre d'émission.

-- Sélectionne le titre de l'émission et l'ID du genre.
SELECT tv_shows.title, tv_show_genres.genre_id
-- Commence par la table tv_shows, car on veut toutes les émissions.
FROM tv_shows
-- Jointure gauche avec tv_show_genres pour inclure même les émissions sans genre.
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Garde UNIQUEMENT les lignes où la correspondance n'a pas été trouvée.
WHERE tv_show_genres.genre_id IS NULL
-- Trie le résultat final comme demandé.
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
