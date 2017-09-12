import random 
cnt=0

def quicksort(a):
	global cnt
	if len(a)<2:
		return a
	p=a.pop(0)
	menores, mayores = [], []
	for e in a:
		cnt+=1
		if e<= p:
			menores.append(e)
		else:
			mayores.append(e)
	return quicksort(menores)+[p]+ quicksort(mayores)

    

#programa principal
a=[4,5,78,2,8]
print(a)
quicksort(a)
print(a)
print(cnt)
