import os

def main():
    folderName=input("文件夹名称:")
    end_Name=input("后缀名(默认jpg):")
    num_Name=input("命名的起始数字:")
#如果文件夹名称为空,指定文件夹名为temps,自动创建一个名为temps的文件夹
#如果名为temps的文件夹已经存在，则抛出异常，显示提示信息
    try:
        if folderName=="":
            folderName="temps"
            os.mkdir(folderName)
    except:
        print("\n文件夹已存在\n将图片拉进temps文件夹里面，然后重新运行一次，文件夹名称输入temps")
        
    if end_Name=="":#如果后缀名为空
        end_Name="jpg"#默认后缀名设置为jpg

#os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    folder = os.listdir(folderName+"/")
    
#如果命名的起始值为空,默认从1开始,如果有起始值,则从设定的起始值开始。  
    try:
        if num_Name=="":
            i=1
        else:
            i=int(num_Name)
    except:
        print("\n起始值只能是数字类型")
        
    for file in folder:
        try:
            os.rename(folderName+"/"+file,folderName+"/"+str(i)+"."+end_Name)
        except:
            print("重名了\n")
        print(file+" => "+str(i)+"."+end_Name)
        i+=1
        
if __name__=="__main__":
    main()
    input("\n按enter退出")
