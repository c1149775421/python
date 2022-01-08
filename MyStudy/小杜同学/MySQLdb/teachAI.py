import MySQLdb
try:
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "user_db", charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    print("----------------------")
    print("欢迎来到小杜训练中心！")
    print("----------------------")
    while True:
        print("\n----------------------------------------------------------------")
        print("输入'teach'进入训练,输入'show'查看所有记录,输入‘exit’退出程序!")
        print("----------------------------------------------------------------")
        command=input("请输入指令：")
        if command=="teach":
            try:
                user = input("输入对小杜说的话：")
                pwd = input("输入小杜的回答：")
                sql = 'insert into user values("'+str(user)+'","'+str(pwd)+'")'#插入数据
                print(sql)
                cursor.execute(sql)
                print("添加成功")
            except:
                print("添加失败")
        if command=="show":
            try:
                cursor.execute("SELECT * from user")
                result = cursor.fetchall()
                for row in result:
                    u = row[0]
                    p = row[1]
                    print("指令=%s,回答=%s" %(u,p))
            except:
                print("查询失败")
        if command=="exit":
            break
    #关闭数据库连接
    db.close()
except:
    print("数据库连接失败")
    input("按enter键退出")
    

