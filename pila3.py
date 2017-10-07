class pila:

    def _init_(self):

        self.pila=[]

    def obtener(self):

        return self.pila.pop()

    def meter(self,e):

        self.pila.insert(0,e)

        return len(self.pila)

    @property

    def longitud(self):

        return len(self.pila)
