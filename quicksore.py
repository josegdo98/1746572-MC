import random 
cnt=0

def quicksort(a):
	global cnt
	if lem(a)<2:
		return 0
	p=a.pop(0)
	menores, mayores = [], []
	for e in a:
		cnt+=1
		if e<= p:
			menores.append(e)
		else:
			mayores.append(e)
	return quicksore(menores)+[p]+ quicksore(mayores)
def rndar(long)
	a = []
	for i in range (long):
		a.append(random,randint(0,long))
	return arr
l=10
while l<10:
	for replica in range(10):
		ori  = rndar (l)
		a = quicksore(ori)
		print(l, cnt, a, ori)
		cnt = 0
	l*=2



