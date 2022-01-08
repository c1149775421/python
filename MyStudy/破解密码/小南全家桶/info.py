with open("密码本.txt","a",encoding="utf-8") as f:
    for i in range(1,1000):
        j=str(i)+"\n"
        f.write("azrj"+j)
        f.flush()
    f.close()
    print("ok")
