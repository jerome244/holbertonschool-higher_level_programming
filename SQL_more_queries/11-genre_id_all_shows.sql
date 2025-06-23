-- 11-genre_id_all_shows.sql
-- List all shows with their genre_id (NULL if no genre), sorted by title and genre_id ascending
-- The database name will be passed as an argument to the mysql command

SELECT
  tv_shows.title,
  tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
ORDER BY
  tv_shows.title ASC,
  tv_show_genres.genre_id ASC;
