import zipfile,time
x=input("请输入压缩包名称：")
try:
    zfile = zipfile.ZipFile(x+'.zip','r')#读取压缩包
except:
    print("\n输入有误")
    pass

try:
    start_time = time.time()#开始时间
    zfile.extractall(path='./'+x,pwd="".encode('utf-8'))#解压
    end_time = time.time()#结束时间
    print("\n解压成功")
    print ('当前破解压缩包花了%s秒'%(end_time-start_time))
except Exception as e:
    print("解压失败")
    pass
