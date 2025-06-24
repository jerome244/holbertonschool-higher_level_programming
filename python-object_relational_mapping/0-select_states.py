#!/usr/bin/python3
"""
0-select_states.py: Connects to a MySQL database and lists all states sorted by their id.

This script takes three arguments: MySQL username, password, and database name.
It uses the MySQLdb module to fetch and display each state as a tuple.
"""

import sys
import MySQLdb


def main():
    """Parse CLI arguments, connect to MySQL, execute query, and print states."""
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Establish connection to the MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cursor = connection.cursor()

    # Retrieve all states ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Clean up database resources
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
