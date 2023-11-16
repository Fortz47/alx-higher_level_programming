#!/usr/bin/python3
"""a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    HOST = 'localhost'
    USR = sys.argv[1]
    PAS = sys.argv[2]
    DB = sys.argv[3]

    try:
        db = MySQLdb.connect(host=HOST, port=3306, user=USR, passwd=PAS, db=DB)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
        rows = cur.fetchall()
        for row in rows:
            print(f'{row}')
    except MySQLdb.Error as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
