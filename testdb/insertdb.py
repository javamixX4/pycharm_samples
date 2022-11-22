import pymysql

conn = None
cur = None

data1 = ""
data2 = ""
data3 = ""
data4 = ""

sql = ""

conn = pymysql.connect(
    host='127.0.0.1',
    user='javamix',
    password='12345678*',
    db='stockdb', charset='utf8'
)
cur = conn.cursor()

while(True):
    data1 = input("사용자 ID를 입력하세요(엔터 클릭 시 종료): ")
    if data1 == "": # 만약 data1에 아무값도 입력받지 않는다면
        break
    data2 = input("사용자이름을 입력하세요")
    data3 = input("이메일을 입력하세요")
    data4 = input("출생연도를 입력하세요")
    sql = "insert into usertable (id, userName, email, birthYear) values('" + data1 + "','" + data2 + "','" + data3 + "',"  + data4 + ")"
    print("SQL >> {0}".format(sql))
    print("SQL :: {query}".format(query=sql))
    cur.execute(sql)
conn.commit()
conn.close()