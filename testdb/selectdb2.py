import pymysql

conn = None
cur = None

data1=""
data2=""
data3=""
data4=""

row = None

conn = pymysql.connect(
    host='127.0.0.1',
    user='javamix',
    password='12345678*',
    db='stockdb', charset='utf8'
)
cur = conn.cursor()

cur.execute("select * from usertable")
print("userID        userName    eMail      BirthYear")
print("-----------------------------------------------")

for (id, name, email, birthYear) in cur:
    print("{id}     {name}      {email}     {birthYear}".format(id=id, name=name, email=email, birthYear=birthYear))
conn.close()