import os
location=input("请输入文件夹名称：")
conf_end=input("是否更改后缀名yes/no:")

if conf_end=="yes":
    inn = input("请输入后缀名:")
else:
    inn="jpg"

folder = os.listdir(location+"/")
i=1
for file in folder:
    inn1=file
    file_end = os.path.splitext(file)[1]
    
    if conf_end=="no":
        inn = file_end
        
    x=os.rename(location+"/"+file,location+"/"+str(i)+"."+inn)
    i+=1
    print(inn1+"  =>  "+str(i)+"."+inn+"\n")
input("按enter退出")
