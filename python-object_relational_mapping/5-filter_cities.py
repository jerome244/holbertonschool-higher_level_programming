#!/usr/bin/python3
"""
5-filter_cities.py: Lists all cities of a given state from the database.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cursor = connection.cursor()

    # Execute a single safe query to get city names for the given state
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Fetch city names and print joined by comma and space
    rows = cursor.fetchall()
    if rows:
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    cursor.close()
    connection.close()
