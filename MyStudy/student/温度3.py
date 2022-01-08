#py
Tempstr = input("输入")
if Tempstr[-1] in ["F", "f"]:
    C = (eval(Tempstr[0:-1]) - 32)/1.8
    print("结果{:.2f}C".format(C))
elif Tempstr[-1] in ["C", "c"]:
    F = 1.8*eval(Tempstr[0:-1]) + 32
    print("结果{:.2f}F".format(F))
else:
    print("错误")
input("按enter键退出")