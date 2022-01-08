x = input("请输入")
if x[-1] in ['F', 'f']:
    C = (eval(x[0:-1]) - 32)/1.8
    print("温度是{:.2f}C".format(C))
elif x[-1] in ['C', 'f']:
    F = 1.8*eval(x[0:-1]) + 32
    print("温度是{:.2f}F".format(F))
else:
    print("格式错误")
input("按enter键退出")