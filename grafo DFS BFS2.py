class Grafo:
	def __init__(self):
		self.V=set()
		self.E=dict()
		self.vecinos=dict()
	def agrega(self,v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v]=set()
	def conecta(self,v,u,peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v,u)]=self.E[(u,v)]=peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)

def BFS(g,ni):

	visitados=[]

	f=fila()

	f.meter(ni)

	while(f.longitud>0):

		na=f.obtener()

		visitados.append(na)

		ln=G.vecinos[na]

		for nodo in ln:

			if nodo not in visitados:

				f.meter(nodo)

				return visitados

def DFS(g,ni):

	f=pila()

	f.meter(ni)

	while(f.longitud>0):

		na=f.obtener()

		visitados.append(na)

		ln=G.vecinos[na]

		for nodo in ln:

			if nodo not in visitados:

				f.meter(nodo)

				return visitados

				






