import time

def main():
    hh=time.strftime('%H')
    mm=time.strftime('%M')
    ss=time.strftime('%S')
    print(time.strftime('{}:{}:{}'.format(hh,mm,ss)))
while True:
    main()
    time.sleep(1)