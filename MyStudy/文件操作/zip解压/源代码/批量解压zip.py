import zipfile,time,os

fileName=input("文件夹名称：")
outName=input("输出到文件夹：")
start_time_all = time.time()#开始时间
file=os.listdir(fileName+"/")#os.listdir遍历所有文件
print(file,"\n")
try:
    os.mkdir(outName)
except:
    print("文件夹已经存在")

for i in range(len(file)):
    try:
        zfile = zipfile.ZipFile(fileName+"/"+file[i],'r')#读取压缩包
        print(file[i])
    except:
        print(file[i],"\n输入有误")
        pass

    try:
        start_time = time.time()#开始时间
        zfile.extractall(path=outName+"/"+file[i],pwd="".encode('utf-8'))#解压命令
        end_time = time.time()#结束时间
        print("解压成功")
        print ('当前压缩包花了%s秒'%(end_time-start_time),"\n")
    except Exception as e:
        print("解压失败")
        pass

end_time_all = time.time()#结束时间
print ('\n全部压缩包总共花了%s秒'%(end_time_all-start_time_all))
