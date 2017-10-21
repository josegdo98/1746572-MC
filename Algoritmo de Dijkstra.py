from heapq import heappop, heappush

from copy import deepcopy



def flatten(L):

    while len(L) > 0:

        yield L[0]

        L = L[1]



class Grafo:

 

    def __init__(self):

        self.V = set() # un conjunto

        self.E = dict() # un mapeo de pesos de aristas

        self.vecinos = dict() # un mapeo

 

    def agrega(self, v):

        self.V.add(v)

        if not v in self.vecinos: # vecindad de v

            self.vecinos[v] = set() # inicialmente no tiene nada

 

    def conecta(self, v, u, peso=1):

        self.agrega(v)

        self.agrega(u)

        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos

        self.vecinos[v].add(u)

        self.vecinos[u].add(v)

 

    def complemento(self):

        comp= Grafo()

        for v in self.V:

            for w in self.V:

                if v != w and (v, w) not in self.E:

                    comp.conecta(v, w, 1)

        return comp



    def shortest(self, v): 

        q = [(0, v, ())] 

        dist = dict() 

        visited = set() 

        while len(q) > 0: 
            (l, u, p) = heappop(q) 
            if u not in visited: 

                visited.add(u) 
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	
            p = (u, p) 
            for n in self.vecinos[u]: 
                if n not in visited: 
                    el = self.E[(u,n)] 

                    heappush(q, (l + el, n, p)) 

        return dist 



    def kruskal(self):

        e = deepcopy(self.E)

        arbol = Grafo()

        peso = 0

        comp = dict()

        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)              nuevo = set()

        while len(t) > 0 and len(nuevo) < len(self.V):

            #print(len(t)) 

            arista = t.pop()

            w = e[arista]    

            del e[arista]

            (u,v) = arista

            c = comp.get(v, {v})

            if u not in c:

                #print('u ',u, 'v ',v ,'c ', c)

                arbol.conecta(u,v,w)

                peso += w

                nuevo = c.union(comp.get(u,{u}))

                for i in nuevo:

                    comp[i]= nuevo

        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)

        return arbol



			

			

g= Grafo()

g.conecta('a','b', 1)

g.conecta('a','c', 1)

g.conecta('a','d', 1)

g.conecta('a','e', 1)

g.conecta('c','e', 1)

g.conecta('c','f', 10)

g.conecta('b','f', 1)



print(g.kruskal())

print(g.shortest('c'))