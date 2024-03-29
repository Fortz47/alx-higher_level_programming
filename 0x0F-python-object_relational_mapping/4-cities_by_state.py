#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

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
        query = "SELECT c.id, c.name, s.name "\
                "FROM `cities` AS c "\
                "JOIN states AS s ON c.state_id = s.id "\
                "ORDER BY c.id"
        cur.execute(query)
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
