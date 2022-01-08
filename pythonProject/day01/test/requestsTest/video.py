import requests,lxml,json,time
from bs4 import BeautifulSoup

r=requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid=241804512",stream=True)
r.encoding='utf-8'
t=BeautifulSoup(r.text,'lxml').find_all("d")
print(len(t))
f=open("评论/pl.txt",mode="a",encoding="utf-8")
print("执行开始".center(len(t)//2,"-"))
start = time.perf_counter()
for i in range(len(t)):
    a = '*' * int(i / 8)
    if i % 2 == 0:
        b = '*' * int(((len(t) - i) / 8) - 1)
    else:
        b = '*' * int((len(t) - i) / 8)
    c = int((i / len(t)) * 100 + 1)
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.01)

    p=t[i].get_text()
    f.write(p+'\n')
    f.flush()
f.close()
