import os,datetime
y=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#年月日 时分秒
d=input("文件夹名称:")
file=r"C:\Users\Administrator\Desktop\\"+d#文件夹路径
os.mkdir(file)#创建文件夹
x=input("文件名:")
s=input("文本内容:")
file_name=file+"\\"+x+".txt"#txt文件路径
f=open(file_name,"a",encoding="utf-8")#创建并打开文件
f.write(y+"\n"+s)#写入当前时间和用户输入的内容
f.flush()#刷新文件
f.close()#关闭文件
input("\n按enter退出")#防止运行完自动关闭窗口
