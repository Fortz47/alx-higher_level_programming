#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

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
        query = "SELECT c.name "\
                "FROM `cities` AS c "\
                "JOIN states AS s ON c.state_id = s.id "\
                "WHERE s.name = %s "\
                "ORDER BY c.id"
        cur.execute(query, (arg,))
        rows = cur.fetchall()
        result = []
        if len(rows):
            result.append(rows[0][0])
        for i in range(len(rows)):
            if (i > 0):
                result.append(f", {rows[i][0]}")
        print(''.join(result))
    except MySQLdb.Error as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
