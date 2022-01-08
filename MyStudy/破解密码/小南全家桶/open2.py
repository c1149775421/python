import zipfile
def main():
    name=input("请输入密码本的名称(默认txt,无需输入后缀):")
    sts=input("请输入压缩包名称(默认zip,无需输入后缀):")
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
        if zfile:
            try:
                zfile.extractall(path='.',pwd=str(arr[i]).encode('utf-8'))
                print("当前密码为:",arr[i])
                break
            except Exception as e:
                print("pass密码:",arr[i])
                pass
if __name__ == "__main__":
    main()
input("\n破解完成,按enter退出")
