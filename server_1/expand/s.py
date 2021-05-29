import pymysql
import os

os.chdir("./../media/img")

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="ZHANGruibin123", database="server_2")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
ii = 0
for dir in os.listdir():
    if os.path.isdir(dir):
        for i in os.listdir(dir):
            img = "img" + "/" + dir + "/" + i
            ii += 1
# 使用 execute()  方法执行 SQL 查询
            cursor.execute(f"insert into expand_image (name, img) values ('{i}', '{img}')")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
db.commit()
print(ii)

# 关闭数据库连接
db.close()

