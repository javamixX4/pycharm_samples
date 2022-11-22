import pymysql

def dbconnect():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='javamix',
        password='12345678*',
        db='stockdb', charset='utf8'
    )
    return conn

def main():
    conn = dbconnect()
    print("success to connect DB")
    conn.close()
    print("success to disconnect DB")

if __name__ == "__main__":
    main()