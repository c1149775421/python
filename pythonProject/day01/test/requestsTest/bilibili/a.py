# url="http://113-100-191-156.mcdn.bilivideo.cn:480/upgcxcode/82/94/253019482/253019482-1-30080.m4s?expires=1606452408&platform=pc&ssig=Xq-EI0k3ILiV9zzgX1UkQQ&oi=236398098&trid=7c1ad5e73f6040a995e609db891c8d84u&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&mcdnid=9000082&mid=0&orderid=0,3&agrr=0&logo=A0000100"
# r2=requests.get(url,stream=True)
# with open("MP4/test.mp4",mode="wb") as f:
#     f.write(r2.content)
#     f.flush()
#     f.close()

import requests,lxml,json,time
from bs4 import BeautifulSoup

r=requests.get("https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=801440908&sort=2&_=1615817256781",stream=True)
r.encoding='utf-8'
t=BeautifulSoup(r.text,'lxml')
print(t)
