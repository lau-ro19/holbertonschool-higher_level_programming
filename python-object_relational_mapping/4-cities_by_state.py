#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Uses only one execute() call with a JOIN operation.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
