-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
WHERE tv_show.title = 'DEXTER'
ORDER BY tv_genres.name ASC;
