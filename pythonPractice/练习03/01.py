def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
a = fact(10)#函数的调用
print(a)#打印返回值
input("按enter键退出")