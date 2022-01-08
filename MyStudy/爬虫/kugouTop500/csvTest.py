array=[]
for i in range(0,500):
    f=open("a.txt","r",encoding="utf-8")
    x=f.read()
    y1=x.split("<-enter->")[i].split("<-space->")[0]
    y2=x.split("<-enter->")[i].split("<-space->")[1]
    y3=x.split("<-enter->")[i].split("<-space->")[2]
    #print(y)
    array.append([y1,y2,y3])
    f.flush()
f.close()

with open("test.csv","w",encoding="utf-8") as f:
    f.write("")
    print("已清空")
    f.flush()
    f.close()

with open("test.csv","a",encoding="utf_8_sig") as f:
    for i in range(0,500):
        bl=array[i]
        for j in range(0,3):
            f.write(bl[j])
            f.write(',')
            print(bl[j])
        f.write("\n")
        f.flush()
    f.close()
