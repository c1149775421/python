for i in range(1,11):
    f=open("test.txt",mode="a",encoding="utf-8")
    f.write("19计网"+str(i)+"班"+"\n")
    f.flush()
    f.close()

f=open("test.txt",mode="r",encoding="utf-8")
result=f.read()
print(result)
f.close()

