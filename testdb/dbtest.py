import pymysql
import sys

conn = None
cur = None

sql = ""
try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='javamix',
        password='12345678*',
        db='stockdb', charset='utf8'
    )
except pymysql.err as E:
    print(f"Error connection to DB : {E}")
    sys.exit(1)

cur = conn.cursor()

sql = 'CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(10), email char(15), birthYear int)'
cur.execute(sql)
conn.commit()

conn.close()
