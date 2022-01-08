arr=[[1,2],[3,4],[5,6]]
x=0
while x<len(arr):
    ii=""
    for i,j in enumerate(arr[x]):
        if i>=len(arr[x])-1:
            ii+=str(j)
        else:
            ii+=str(j)+","
    print(ii)
    x+=1
