import pymysql as pm
conn = pm.connect(host='127.0.0.1', port=3306,
                  user='root', password='040521', db='pm')

cursor = conn.cursor()

try:
    sql = "show tables;"
    row_count = cursor.execute(sql)
    print('sql 语句执行影响%d' % row_count)
#     sql = "create table student;"
#     sql = "selete  * from student"
except:
    print('问题')


cursor.close()

conn.close()
