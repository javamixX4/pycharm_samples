import mariadb
import sys

def dbconnect():
    try :
        conn = mariadb.connect(
            host='127.0.0.1',
            user='javamix',
            password='12345678*',
            db='stockdb',
            port=3306
        )
    except mariadb.Error as e:
        print("Error Connecting to MariaDB : {err}".format(err=e))
        sys.exit(1)
    return conn

def main():
    conn = dbconnect()
    print("success to connect DB")
    conn.close()
    print("success to disconnect DB")


if __name__ == "__main__":
    main()
