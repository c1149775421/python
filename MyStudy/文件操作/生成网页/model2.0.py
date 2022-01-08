x=input("你的网页文件想叫什么名字:")
t=input("输入网页标题:")
if t=="":
    t="this is a title"
sts='<!DOCTYPE html>\n <html>\n \t<head>\n \t\t<meta charset="utf-8">\n \t\t<title>'+t+'</title>\n\t\t \n\t</head>\n \t<body>\n\t\t this is a page \n\t</body>\n </html>'
with open(x+".html","w",encoding="utf-8") as w:
    w.write(sts)
    print("成功生成了网页模板")
    w.flush()
    w.close()
input("enter")
