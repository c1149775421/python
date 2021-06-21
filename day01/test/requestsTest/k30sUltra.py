import requests,lxml,json,re,time
from bs4 import BeautifulSoup
r_all=requests.get("https://www.mi.com/p/1915.html")
r_all.encoding='utf-8'
# pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
t=BeautifulSoup(r_all.text,'lxml').find_all("img",class_="thumb")
ii=len(t)

imgArr=[]
for i in range(ii):
    x=t[i].attrs["data-src"]
    imgArr.append(x)
# print(imgArr)
print("执行开始".center(len(imgArr)//2,"-"))
start = time.perf_counter()
for j in range(len(imgArr)):
    a = '*' * int(j/2)
    if j%2==0:
        b = '*' * int(((len(imgArr) - j)/2)-1)
    else:
        b = '*' * int((len(imgArr) - j)/2)
    c = int((j/len(imgArr))*100+1)
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')

    r=requests.get(imgArr[j])
    try:
        f=open("img/"+str(j+1)+".png",mode='wb')
        f.write(r.content)
        f.flush()
        f.close()
    except Exception as e:
        print(e)