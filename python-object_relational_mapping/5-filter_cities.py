#!/usr/bin/python3
"""Lists all cities of a given state from the database."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (argv[4],)
    )
    names = cur.fetchall()
    # prints names comma-separated
    print(", ".join([n[0] for n in names]))
    cur.close()
    conn.close()
