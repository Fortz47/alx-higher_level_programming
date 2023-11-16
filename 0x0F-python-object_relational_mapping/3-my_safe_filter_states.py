#!/usr/bin/python3
"""script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
and handles SQL Injection"""

import MySQLdb
import sys

if __name__ == '__main__':

    HOST = 'localhost'
    USR = sys.argv[1]
    PAS = sys.argv[2]
    DB = sys.argv[3]
    arg = sys.argv[4]

    try:
        db = MySQLdb.connect(host=HOST, port=3306, user=USR, passwd=PAS, db=DB)
        cur = db.cursor()
        query = "SELECT * FROM states where name = %s"
        cur.execute(query, (arg,))
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
