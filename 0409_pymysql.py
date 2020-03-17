import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='test',
    charset='utf8'
)
cursor = connect.cursor()
sql = "insert into student values('test23', 223)"
cursor.execute(sql)
cursor.execute('select * from student')
print cursor.fetchall()
connect.commit()
cursor.close()
connect.close()