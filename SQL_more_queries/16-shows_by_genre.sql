-- 16-shows_by_genre.sql
-- List all shows and their genres, showing NULL for shows without any linked genres
-- Results sorted by show title and genre name ascending
-- The database name will be passed as an argument to the mysql command

SELECT
  s.title,
  g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
ORDER BY
  s.title ASC,
  g.name ASC;
