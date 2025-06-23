-- 12-no_genre.sql
-- List all shows without a genre linked, showing title and genre_id (NULL)
-- Results sorted by title and genre_id ascending
-- The database name will be passed as an argument to the mysql command

SELECT
  tv_shows.title,
  tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
WHERE
  tv_show_genres.genre_id IS NULL
ORDER BY
  tv_shows.title ASC,
  tv_show_genres.genre_id ASC;
