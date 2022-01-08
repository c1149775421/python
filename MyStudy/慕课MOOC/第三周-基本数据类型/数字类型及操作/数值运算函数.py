#abs(x)，绝对值，x的绝对值
print("绝对值",abs(-10.01))

#divmod(x,y)，商余，(x//y,x%y)，同时输出商和余数
#例如：divmod(10,3)结果为(3,1)
print("商余",divmod(10,3))

#pow(x,y[,z])，幂余，(x**y)%z，[..]表示参数z可以省略
powTest=pow(3,pow(3,99),10000)
print("幂余",powTest)

#round(x,d)，四舍五入函数，d是保留的小数位，默认值为0
print("四舍五入",round(-10.123,2))

#max(x1,x2,...,xn)，最大值，返回x1,x2,...,xn中的最大值，n不限
print("最大值=",max(1,9,5,4,3))

#min(x1,x2,...,xn)，最小值，返回x1,x2,...,xn中的最小值，n不限
print("最小值=",min(1,9,5,4,3))

#int(x)，将x变成整数，舍弃小数部分
print("浮点型",int(123.45))
print("字符型",int("123"))

#float(x)，将x变成浮点数，增加小数部分
print("整数型转浮点型",float(12))
print("字符型转浮点型",float("1.23"))

#complex(x)能变成复数类型
print("复数类型",complex(12))
