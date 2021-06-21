import requests,lxml,json,time
from bs4 import BeautifulSoup
r=requests.get("https://wenku.baidu.com/view/7f1c192e64ce0508763231126edb6f1aff0071af.html")
t=BeautifulSoup(r.text,'lxml')
with open("评论/项目计划书.txt",mode="a",encoding="utf-8") as f:
    f.write(str(t))
    f.flush()
    f.close()
# print(t)