"""
round(x,d):对x四舍五入，d是小数保留的位数
浮点数运算及比较用round()函数辅助
不确定尾数一般发生在10的-16次方左右，round()十分有效
"""
a=round(0.1+0.2,1)
print(a)


"""
使用字母e或E作为幂的符号，以10为基数，格式如下:
<a>e<b>  表示a*10的b次方
例如以下运算:值为0.0043，960000.0
"""
b=4.3e-3
print(b)

b2=9.6E5
print(b2)

z=1.23e-4+5.6e89j
print("实部=",z.real)
print("虚部",z.imag)

c=10/3
c2=10//3
print("10除3=",c)
print("10整数除3=",c2)

#整数->浮点数->复数
#例如：整数+浮点数=浮点数
x=123+4.0
print(x)
