class fila:





     def __init__(self):

            self.fila=[ ]



     def obtener(self):

            return self.fila.pop()



     def meter(self,e):

            self.fila.insert(0,e)

            return len(self,fila)



     @property



     def longitud(self):

            return len(self.fila)