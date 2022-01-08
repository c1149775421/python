import MySQLdb,time,os,pygame,speech
import requests,json,lxml
from bs4 import BeautifulSoup
try:
    db = MySQLdb.connect("localhost", "root", "root", "user_db", charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT * from user")
    result = cursor.fetchall()
    #print(len(result))
except:
    print("数据库连接失败，只能使用基础功能")

def main(entry):
    def weather():
        r = requests.get('http://tianqi.2345.com/pc/PcIndex/guangzhou/59287')
        r.encoding = 'utf-8'
        t = BeautifulSoup(r.text, 'lxml').find("div", class_="info-box-wrap-left")

        r2 = requests.get('http://tianqi.2345.com/guangzhou1d/59287.htm')
        r2.encoding = 'utf-8'
        t2 = BeautifulSoup(r2.text, 'lxml')

        city = t.find("div",class_="location").find("em").get_text().replace('\n','').replace('\t','').replace('\r','')#城市
        date_all = t.find("p",class_="date")  # 获得总数据
        d = BeautifulSoup(str(date_all), 'lxml')  # 处理总数据
        date = str(d.find("p")).split("<b>")[0].split(">")[1]  # 日期
        day = d.find("b").get_text()  # 星期几
        lunar = str(d.find("p")).split("</b>")[1].split("<em>")[0]  # 农历
        time = d.find("em").get_text()  # 发布时间

        detail = t.find("div", class_="wea-detail-index")  # 获得总数据
        d2 = BeautifulSoup(str(detail), 'lxml')  # 处理总数据
        wd = d2.find("a", class_="wea-info-index").get_text().replace('\n', '').replace('\t', '').replace('\r','')  # 当前温度
        tq = d2.find("a", class_="wea-other-a-we").get_text().replace('\n', '').replace('\t', '').replace('\r','')  # 当前天气
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

    ent=entry
    arr = ["当前时间", "现在时间", "时间", "现在几点了","今天几号",
           "当前日期","日期","今天天气","天气预报","天气",
           "查天气","今日天气","有点甜","发如雪"]
    da = "小杜:"
    flag = False

    if ent=="exit":
        speech.say("正在退出")
        exit(0)

    if ent=="当前时间" or ent=="现在时间" or ent=="时间" or ent=="现在几点了":
        datetime=time.strftime("%H:%M:%S")
        print(da, "当前北京时间", datetime)
        speech.say("当前北京时间"+datetime)
        flag = True

    if ent=="今天几号" or ent=="当前日期" or ent=="日期":
        date=time.strftime("%Y-%m-%d")
        print(da,"今天是",date)
        speech.say("今天是"+date)
        flag = True

    if ent=="今天天气" or ent=="天气预报" or ent=="天气" or ent=="查天气" or ent=="今日天气":
        try:
            weather()
        except:
            print("天气数据获取失败,请检查网络连接!")
            speech.say("天气数据获取失败,请检查网络连接!")
        flag = True

    pygame.mixer.init()
    if ent=="有点甜":
        pygame.mixer.music.load("music/有点甜-汪苏泷_By2.mp3")
        print("开始播放:有点甜-汪苏泷_By2")
        speech.say("开始播放:有点甜-汪苏泷-By2")
        pygame.mixer.music.play()
        flag = True
        print("输入'pause'或者'stop'可以暂停播放哦!")
    elif ent=="发如雪":
        pygame.mixer.music.load("music/周杰伦-发如雪.mp3")
        print("开始播放:周杰伦-发如雪")
        speech.say("开始播放:周杰伦-发如雪")
        pygame.mixer.music.play()
        flag = True
        print("输入'pause'或者'stop'可以暂停播放哦!")

    if ent=="pause" or ent=="stop":
        pygame.mixer.music.pause()
        print("输入'unpause'或者'play'可以继续播放哦!")
        flag = True
    if ent=="unpause" or ent=="play":
        pygame.mixer.music.unpause()
        print("输入'pause'或者'stop'可以暂停播放哦!")
        flag = True

    if ent=="你会什么" or ent=="你会做什么" or ent=="你会干啥":
        print(da,"我会的都在这里了>>>")
        speech.say("我会的都在这里了")
        try:
            for i in result:
                arr.append(i[0])
                flag = True
            print(arr)
        except:
            print(arr)

    try:
        for row in result:
            if ent == row[0]:
                flag = True
                print(da, row[1])
                speech.say(row[1])
                break
            # elif ent == row[1]:
            #     flag = True
            #     print(da, row[0])
            #     break
    except:
        if flag==False:
            print("---------------------------")
            print("数据库未连接，当前只能使用基础功能")
            speech.say("数据库未连接，当前只能使用基础功能")
            print("Tips:输入'exit'可以结束程序哦!")
            print("---------------------------")
        flag = True

    if flag == False:
        print(da, "抱歉，找不到结果，小杜还在成长中...")
        speech.say("抱歉，找不到结果，小杜还在成长中")
        print("Tips:输入'exit'可以结束程序哦!")

if __name__=="__main__":
    print("-----------------------------------------")
    print("我是小杜，可以问我天气、时间、日期,输入音乐名可播放")
    print("-----------------------------------------")
    while True:
        entry = input("\n您请说：")
        main(entry)
    try:
        db.close()
    except:
        exit(0)
