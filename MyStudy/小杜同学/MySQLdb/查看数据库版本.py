import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "user_db", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用cursor.execute()方法执行SQL语句
cursor.execute("SELECT VERSION()")
# cursor.execute("SELECT * from user")

#sql = "insert into user values('hello','world')"#插入数据
#cursor.execute(sql)
#print("添加成功")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

# ent = input("输入关键字：")
# result = cursor.fetchall()
# #print(len(result))
# for row in result:
#     if ent==row[0]:
#         print(row[1])
#         break
#     elif ent==row[1]:
#         print(row[0])
#         break
    # user = row[0]
    # pwd = row[1]
    # print("user=%s,pwd=%s" %(user,pwd))

print("Database version : %s " % data)
input("enter")
# 关闭数据库连接
db.close()
