import requests
import time
from bs4 import BeautifulSoup
import lxml

def get_html(url):
    '''
    获得 HTML
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53\
        7.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return


def get_infos(html):
    '''
    提取数据
    '''
    html = BeautifulSoup(html,'lxml')
    # 排名
    ranks = html.find_all('span',class_='pc_temp_num')
    # 歌手 + 歌名
    names = html.find_all('a',class_='pc_temp_songname')
    # 播放时间
    times = html.find_all('span',class_='pc_temp_time')

    # 打印信息
    for r,n,t in zip(ranks,names,times):
        r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
        n = n.get_text()
        t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
        data = {
            '排名': r,
            '歌名-歌手': n,
            '播放时间': t
        }
        #定义变量
        num=data['排名']
        name=data['歌名-歌手']
        time=data['播放时间']
        
        #控制台打印输出
        print(num+'\t'+name+'\t'+time+'\n')
        
        #文件写入内容(js数据源)
        f=open("a.txt",mode="a",encoding="utf-8")
        f.write(num+'<-space->'+name+'<-space->'+time+'<-enter->')
        f.flush()
        f.close()
        #文件写入内容(查看版)
        f=open("b.txt",mode="a",encoding="utf-8")
        f.write(num+'\t'+name+'\t'+time+'\n')
        f.flush()
        f.close()

def main():
    #清空文件写入内容(js数据源)
    f=open("a.txt",mode="w",encoding="utf-8")
    f.write("")
    f.flush()
    f.close()
    #清空文件写入内容(查看版)
    f=open("b.txt",mode="w",encoding="utf-8")
    f.write("")
    f.flush()
    f.close()
    print("已清空")
    
    '''
    主接口
    '''
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'
                .format(str(i)) for i in range(1, 24)]
    for url in urls:
        html = get_html(url)
        get_infos(html)
        time.sleep(1)

if __name__ == '__main__':
    main()

