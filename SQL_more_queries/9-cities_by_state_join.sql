-- 9-cities_by_state_join.sql
-- List all cities with their state names using a single SELECT, sorted by cities.id ascending
-- The database name will be passed as an argument to the mysql command

SELECT cities.id, cities.name, states.name
FROM cities
-- JOIN states ON cities.state_id = states.id
-- This line links each city to its corresponding state by matching the state_id in the cities table
-- with the id in the states table, allowing retrieval of the state's name for each city.
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
