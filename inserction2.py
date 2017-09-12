cnt = 0

def orden.por.inserccion(array):
	global cnt
	for indice in range (1,len(array)):
		valor=array[indice]
		i=indice-1
                while i>=0:
			cnt+=1
                	if valor<lista[i]:
                        	array[i+1]=array[i]
				array[i]=valor
                            	i-=1
                         else:
                             	break
              return array

                       
                

                