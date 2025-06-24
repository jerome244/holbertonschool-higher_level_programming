#!/usr/bin/python3
"""3-my_safe_filter_states.py: Lists all states with a given name from the database safely against SQL injection."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

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

    # Safe query using parameterized arguments to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Print matching states
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()
