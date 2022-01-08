import zipfile,time,os
fileName=input("文件夹名称(默认为1)：")
outName=input("输出到文件夹(默认output)：")
start_time_all = time.time()#开始时间
print("<-------------------------------------->")
if fileName=="":
    try:
        fileName=os.mkdir("1")
    except:
        fileName="1"
        print("\n\t默认文件夹",fileName,"已存在")
else:
    try:
        os.mkdir(fileName)
    except:
        print("\n\t文件夹",fileName,"已存在")
            
if outName=="":
    try:
        outName="output"
        os.mkdir(outName)
    except:
        print("\t输出文件夹",outName,"已存在")
else:
    try:
        os.mkdir(outName)
    except:
        print("\t输出文件夹",outName,"已存在")
            
def main():
    file=os.listdir(fileName+"/")#os.listdir遍历所有文件
    print("\t压缩包总共有：",len(file),"个","\n")
    print("<-------------------------------------->")
    ok=0#计算解压成功数的变量
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
            print ('当前压缩包花了%s秒'%(end_time-start_time))
            print("--------------------")
            ok+=1
        except Exception as e:
            print("解压失败")
            print("--------------------")
            ok-=1
            pass
    print("\n解压成功",ok,"个")
         
if __name__=="__main__":
    main()
    end_time_all = time.time()#结束时间
    print ('全部压缩包总共花了%s秒'%(end_time_all-start_time_all))
    input("按enter键退出")





    


