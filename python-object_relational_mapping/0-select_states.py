#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


def main():
    """Connects to MySQL and lists all states ordered by id."""
    # Unpack credentials and database name
    options = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3],
        "charset": "utf8"
    }

    # Establish connection and create cursor
    conn = MySQLdb.connect(**options)
    cur = conn.cursor()

    # Execute query and fetch results
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
