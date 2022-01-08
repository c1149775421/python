import requests,json,lxml
from bs4 import BeautifulSoup
r=requests.get('http://tianqi.2345.com/pc/PcIndex/guangzhou/59287')
r.encoding='utf-8'
t=BeautifulSoup(r.text,'lxml').find("div",class_="info-box-wrap-left")

r2=requests.get('http://tianqi.2345.com/guangzhou1d/59287.htm')
r2.encoding='utf-8'
t2=BeautifulSoup(r2.text,'lxml')

def weather():
    city=t.find("div",class_="location").find("em").get_text().replace('\n','').replace('\t','').replace('\r','')#城市
    date_all = t.find("p", class_="date")  # 获得总数据
    d = BeautifulSoup(str(date_all), 'lxml')  # 处理总数据
    date = str(d.find("p")).split("<b>")[0].split(">")[1]  # 日期
    day = d.find("b").get_text()  # 星期几
    lunar = str(d.find("p")).split("</b>")[1].split("<em>")[0]  # 农历
    time = d.find("em").get_text()  # 发布时间

    detail = t.find("div", class_="wea-detail-index")  # 获得总数据
    d2 = BeautifulSoup(str(detail), 'lxml')  # 处理总数据
    wd = d2.find("a", class_="wea-info-index").get_text().replace('\n', '').replace('\t', '').replace('\r', '')  # 当前温度
    tq = d2.find("a", class_="wea-other-a-we").get_text().replace('\n', '').replace('\t', '').replace('\r', '')  # 当前天气
    kqzl = d2.find("a", class_="wea-aqi-tip-index").get_text().replace('\n', '').replace('\t', '').replace('\r','')  # 空气质量

    ul = t.find("ul", class_="wea-info-tip")  # 获得总数据
    d3 = BeautifulSoup(str(ul), 'lxml')  # 处理总数据
    wd_min_max = d3.find_all("li")[0].get_text().replace('\n', '').replace('\t', '').replace('\r', '')  # 最高温和最低温
    sd = d3.find_all("li")[1].get_text().replace('\n', '').replace('\t', '').replace('\r', '')  # 湿度
    zwx = d3.find_all("li")[2].get_text().replace('\n', '').replace('\t', '').replace('\r', '')  # 紫外线
    tips = t.find("a", class_="wea-real-time-tips").get_text().replace('\n', '').replace('\t', '').replace('\r','')  # 温馨提示

    real_data = t2.find("ul", class_="real-data")  # 天气详情总数据
    feng = real_data.find_all("span")[0].get_text()  # 风力等级
    hpa = real_data.find_all("span")[3].get_text()  # 气压

    print("最新数据于:", time)  # 发布时间
    print(date, day, lunar)
    print(city, tq, wd, "\t", kqzl)
    print(feng, "\t", hpa)
    print(wd_min_max, sd, zwx)
    print(tips)

if __name__=="__main__":
    try:
        weather()
    except:
        print("天气数据获取失败,请检查网络连接!")