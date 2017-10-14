def primo(n): 
    global cnt

    for i in range (2,round(n**(1/2)+1)):
            cnt=cnt+1
            if ((n%i)==0):
                return ("No es primo")
            
    return ("Es primo")


for i in range(2,50):
    cnt=0
    primo(i)
    print(i,cnt)