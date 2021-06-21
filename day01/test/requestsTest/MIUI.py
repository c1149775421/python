import requests,lxml,json
from bs4 import BeautifulSoup
r=requests.get("http://www.miui.com/shuaji-393.html")
t=BeautifulSoup(r.text,'lxml')

print("输入:[1.下载刷机工具,2.下载解锁工具]")
str=input("请输入指令：")
if str=="show":
    all=t.find("div",class_="intro").find_all("a")
    for i in range(len(all)):
        x=t.find("div",class_="intro").find_all("a")[i].get_text()
        y=t.find("div",class_="intro").find_all("a")[i].attrs["href"]
        print(x,"http:"+y)
elif str=="下载刷机工具" or str=="1":
    print("开始下载通用刷机工具miflash>>>")
    print(t.find("div", class_="intro").find_all("span")[0].get_text())
    miflash=t.find("div",class_="intro").find_all("a")[0].attrs["href"]
    d=requests.get(miflash,stream=True)
    with open("MIUI/miflash.zip",mode="wb") as f:
        f.write(d.content)
        print("下载完成")
        f.flush()
        f.close()
elif str=="下载解锁工具" or str=="2":
    print("开始下载解BL锁工具>>>")
    BL="http://miuirom.xiaomi.com/rom/u1106245679/4.5.813.51/miflash_unlock-4.5.813.51.zip"
    d2=requests.get(BL,stream=True)
    with open("MIUI/BootLoader.zip",mode="wb") as f2:
        f2.write(d2.content)
        print("下载完成")
        f2.flush()
        f2.close()
else:
    print("指令有误，请重试")