#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state,)
    )
    rows = cursor.fetchall()
    if rows:
        print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
