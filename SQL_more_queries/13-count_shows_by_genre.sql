-- 13-count_shows_by_genre.sql
-- List all genres and the number of shows linked to each, sorted by number of shows descending
-- Do not display genres with zero shows
-- The database name will be passed as an argument to the mysql command

SELECT
  g.name AS genre,
  COUNT(g.id) AS number_of_shows
FROM tv_show_genres AS tsg
JOIN tv_genres AS g ON tsg.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
