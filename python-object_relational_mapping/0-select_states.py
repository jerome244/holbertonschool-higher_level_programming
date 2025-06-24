#!/usr/bin/python3
"""
0-select_states.py: Lists all states from the specified MySQL database.

Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import sys
import MySQLdb


def main():
    """Connects to MySQL, retrieves all states ordered by id, and prints each row as a tuple."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    main()
