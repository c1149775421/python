for i in range(0,500):
    f=open("a.txt",mode="r",encoding="utf-8")
    x=f.read()
    print(x.split("<-enter->")[i])
    f.flush()
f.close()

q=open("c.html",mode="w",encoding="utf-8")
q.write("")
print("清空了")
q.flush()
q.close()

f2=open("c.html",mode="a",encoding="utf-8")
f2.write("<html>\n <head>\n <meta charset='UTF-8'>\n <title>test</title>\n </head>\n <body>\n")
f2.flush()
f2.close()

f2=open("c.html",mode="a",encoding="utf-8")
for i in range(0,500):
    f2.write("<p>")
    f2.write(x.split("<-enter->")[i])
    f2.write("</p>\n")
    f2.flush()
f2.close()

f2=open("c.html",mode="a",encoding="utf-8")
f2.write("</body>\n </html>")
f2.flush()
f2.close()
