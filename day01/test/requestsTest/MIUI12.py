import requests,lxml,json,time
from bs4 import BeautifulSoup
r=requests.get("https://home.miui.com/")
r.encoding='utf-8'
t=BeautifulSoup(r.text,'lxml')
# with open("评论/02.txt",mode="a",encoding="utf-8") as f:
#     f.write(str(t))
#     f.flush()
#     f.close()
print(t)