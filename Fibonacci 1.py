def fibo(n):

    global cnt

    cnt=0

    if n==0 or n==1:

        return (1)

    

    r,r1,r2=0,1,1

    for i in range (2,n+1):

        cnt+=1

        r=r1+r2

        r2=r1

        r1=r

    return r,cnt







for i in range (2, 40): 

	cnt=0

	print(i, fibo(i), cnt )

