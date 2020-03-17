import pymysql


def getLevel(score):
    result = ''
    print score
    if score >= 90:
        result = 'Best'
    elif score >= 80:
        result = 'Good'
    elif score >= 70:
        result = 'Middle'
    elif score >= 60:
        result = 'just so so'
    else:
        result = 'bad'
    return result


def connectDB(sql, type='query'):
    connect = pymysql.Connect(
        host="localhost",
        port=3306,
        user='root',
        passwd='root',
        db='test',
        charset='utf8'
    )
    cursor = connect.cursor()
    cursor.execute(sql)
    if type == 'query':
        return cursor.fetchall()
    cursor.close()
    connect.close()
    return None

if __name__ == "__main__":
    stu_list = connectDB('select * from stu_score')
    print stu_list
    print getLevel(stu_list[1][3])