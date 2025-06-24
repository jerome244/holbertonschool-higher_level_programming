#!/usr/bin/python3
"""
4-cities_by_state.py: Lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

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

    # Execute a single query to join cities and states
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Print each city tuple
    for city in cursor.fetchall():
        print(city)

    cursor.close()
    connection.close()
