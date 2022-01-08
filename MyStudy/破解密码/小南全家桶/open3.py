import zipfile,time
def main():
    name=input("请输入密码本的名称(默认txt,无需输入后缀):")
    sts=input("请输入压缩包名称(默认zip,无需输入后缀):")
    start_time = time.time()
    arr=[]
    with open(name+".txt","r",encoding="utf-8") as f:
        for i in range(1,99999999):
            x=f.readline()
            y=x.split("\n")[0]
            arr.append(y)
            f.flush()
            if y=="":break
            #print(y)
        f.close()

    zfile = zipfile.ZipFile(sts+'.zip','r')
    for i in range(0,len(arr)):
        password=arr[i]
        print("\n当前密码:"+password)
        if zfile:
            try:
                print("正在解压...")
                zfile.extractall(path='./01',pwd=str(password).encode('utf-8'))
                print("\n正确密码为:",password)
                end_time = time.time()
                print ('当前破解压缩包花了%s秒'%(end_time-start_time))
                break
            except Exception as e:
                if arr[i]=="":
                    print("破解不成功,扩充一下密码库吧!")
                else:
                    print("pass密码:",password)
                    pass
if __name__== "__main__":
    main()
input("\n执行完成,按enter退出")
