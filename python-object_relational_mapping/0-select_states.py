#!/usr/bin/python3
"""
0-select_states script: lists all states from the specified MySQL database.
"""
import MySQLdb
import sys

def main():
    """Connect to MySQL, retrieve all states, and print each as a tuple."""
    # Unpack command-line arguments
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Establish connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password,
                         db=database, charset="utf8")
    cursor = db.cursor()

    # Execute query and fetch results
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
