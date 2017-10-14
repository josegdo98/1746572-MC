arr={}
cnt=0
def fibonacci(n):
    global arr, cnt
    cnt+=1
    if n==0 or n==1:
        return(1)
    if n in arr:
        return arr[n]
    else:
        val=fibonacci(n-2)+fibonacci(n-1)
        arr[n]=val
        return val

for i in range(2,40):
    cnt=0
    print(i,fibonacci(i),cnt)
