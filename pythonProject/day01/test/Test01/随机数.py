import random,time
# for i in range(20):
#     x=random.randrange(10,100,5)#10到100的数，间隔5
#     print(x)
i = 0
while True:
    if i >= 7:
        break
    city=random.choice(['北京','上海','广州','深圳'])
    if city == "广州":
        print("天道酬勤")
    elif city == "深圳":
        print("人定胜天")
    elif city == "上海":
        print("五湖四海")
    elif city == "北京":
        print("八方来贺")
    time.sleep(2)
    i+=1