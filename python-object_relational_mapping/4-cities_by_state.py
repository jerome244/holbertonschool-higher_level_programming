#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states "
        "ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
