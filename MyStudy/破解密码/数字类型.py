import zipfile,time,sys
start_time = time.time()
def extract():
  zfile = zipfile.ZipFile('IdonKnow.zip')#读取压缩包，如果用必要可以加上'r'
  for num in range(1,99999,1):
    try:
      pwd = str(num)
      zfile.extractall(path='.',pwd=pwd.encode('utf-8'))
      print ("当前压缩密码为：",pwd)
      end_time = time.time()
      print ('单线程破解压缩包花了%s秒'%(end_time-start_time))
      sys.exit(0)
    except Exception as e:
      pass
if __name__=="__main__":
  extract()