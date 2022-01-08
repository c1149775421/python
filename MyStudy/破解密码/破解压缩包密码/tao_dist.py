import random,zipfile,time,sys
 
class MyIter():
  cset = '0123456789'
  def __init__(self,min,max):#迭代器实现初始方法，传入参数
    if min < max:
      self.minlen = min
      self.maxlen = max
    else:
      self.ninlen = max
      self.maxlen = min
  def __iter__(self):#直接返回slef实列对象
    return self
  def __next__(self):#通过不断地轮循，生成密码
    rec = ''
    for i in range(0,random.randrange(self.minlen,self.maxlen+1)):
      rec += random.choice(MyIter.cset)
    return rec
def extract():
  sts=input("请输入文件名:")
  sts3=input("如果知道密码的开头就填:")
  sts4=input("密码最短多少位数:")
  sts2=input("密码最长多少位数:")
  start_time = time.time()
  zfile = zipfile.ZipFile((sts+'.zip'),'r')
  for password in MyIter(int(sts4),int(sts2)):#随机迭代出1~4位数的密码，在不明确位数的时候做相应的调整
    if zfile:
      try:
        zfile.extractall(path='.',pwd=str(sts3+password).encode('utf-8'))
        print ("当前压缩密码为：",(sts3+password))
        end_time = time.time()
        print ('当前破解压缩包花了%s秒'%(end_time-start_time))
        input("\n破解完成,按enter退出")
        sys.exit(0)
      except Exception as e:
        print ('pass密码：',(sts3+password))
        pass
if __name__=="__main__":
  extract()

