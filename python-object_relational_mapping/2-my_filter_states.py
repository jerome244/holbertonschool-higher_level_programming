#!/usr/bin/python3
"""Lists all states with a given name from the database."""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        sys.exit(1)
    user, passwd, db, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=user, passwd=passwd, db=db, charset="utf8"
    )
    cur = conn.cursor()

    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
