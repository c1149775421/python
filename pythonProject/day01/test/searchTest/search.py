while True:
    f=open("a.txt", mode="r", encoding="utf-8").read()
    #print(f)
    x=f.split("^")
    #print(x)
    o = False
    ent=input("请输入关键字(0退出)：")
    for i in range(len(x)-1):
        y=x[i].split("-")
        #print(y)
        if ent == y[0]:
            print(y[1])
            o = True
            break
        elif ent == y[1]:
            print(y[0])
            o = True
            break
    if ent==str(0):
        break
    if o==False:
        print("没有找到\n")