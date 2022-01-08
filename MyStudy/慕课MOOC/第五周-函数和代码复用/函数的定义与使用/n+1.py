def fact(n):
    s=1
    for i in range(1,n+1):
        #s*=i
        s=s*i
    return s
y=fact(5)
print(y)

