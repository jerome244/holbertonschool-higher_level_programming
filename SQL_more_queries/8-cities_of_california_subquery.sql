-- 8-cities_of_california_subquery.sql
-- List all cities of California without using JOIN, sorted by cities.id ascending
-- The database name will be passed as an argument to the mysql command

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
