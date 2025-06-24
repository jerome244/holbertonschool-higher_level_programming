#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv


def main():
    """Connects to the database and prints cities for the given state."""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (argv[4],),
    )
    rows = cur.fetchall()
    names = [r[0] for r in rows]
    print(", ".join(names))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
