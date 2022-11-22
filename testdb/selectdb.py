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

while(True):
    row = cur.fetchone()
    if row == None:
        break

    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("{id}     {name}      {email}     {birthYear}".format(id=data1, name=data2, email=data3, birthYear=data4))
conn.close()