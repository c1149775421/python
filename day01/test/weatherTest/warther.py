import requests,json,lxml
from bs4 import BeautifulSoup
#改城市接口就行，固定搭配
r0=requests.get('http://www.weather.com.cn/data/sk/101280103.html')
r0.encoding='utf-8'
#拿取整个网页的数据
r=requests.get('http://www.weather.com.cn/weather1d/101280101.shtml')
r.encoding='utf-8'
# print(r.text)
#拿取类名为t的div标签里面的数据
t=BeautifulSoup(r.text,'lxml').find("div",class_='t')
tem=t.find("p",class_='tem').get_text().replace('\n','').replace('\t','').replace('\r','')#温度
wea=t.find("p",class_='wea').get_text().replace('\n','').replace('\t','').replace('\r','')#天气
win=t.find("p",class_='win').get_text().replace('\n','').replace('\t','').replace('\r','')#风力
print("广州"+r0.json()['weatherinfo']['city'],
      "今天"+wea,tem,r0.json()['weatherinfo']
      ['WD'],win)
