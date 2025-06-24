#!/usr/bin/python3
"""
0-select_states script: lists all states from the specified MySQL database.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL, retrieve all states, and print each as a tuple."""
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd,
                         db=db_name, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
