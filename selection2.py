def selection(arr):
	for i in range(0,len(arr)-1):
		val = 1
 		for j in range(i+1,len(arr)):
  			if arr[j]< arr[val]:
				val = j
 		if val != i:
			aux = arr[i]
			arr[i]=arr [val]
			arr [val]=aux
	return arr

A=[5,4,7]
print(A)
selection(a)
print(a)