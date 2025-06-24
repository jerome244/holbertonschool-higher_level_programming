#!/usr/bin/python3
"""
1-filter_states.py: Lists all states with name starting with 'N' from the database.

Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
from sys import argv


def main():
    """Connect to MySQL and print states whose name starts with 'N'."""
    # Unpack arguments
    user, passwd, db_name = argv[1], argv[2], argv[3]

    # Connect to database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()

    # Execute query filtering names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
