import requests,lxml,json
from bs4 import BeautifulSoup
r=requests.get("http://www.baidu.com")
r.encoding='utf-8'
t=BeautifulSoup(r.text,'lxml').get_text()
print(t)
input("")
