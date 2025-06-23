-- 14-my_genres.sql
-- List all genres of the show Dexter, sorted by genre name ascending
-- The database name will be passed as an argument to the mysql command

SELECT g.name
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id
JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
