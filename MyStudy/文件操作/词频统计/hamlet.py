def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()#全部变成小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}·~‘’':
        txt=txt.replace(ch," ")#符号替换为空格
    return txt

hamletTxt=getText()
words=hamletTxt.split()#默认空格
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
input("enter")
