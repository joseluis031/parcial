class animal:
    def __init__(self, tipo):
        self.tipo = tipo
        
class mamifero(animal): #utilizo la herencia multiple
    def __init__(self,tipo,mamifero):
        self.mamifero = mamifero
        animal.__init__(self, tipo)
        
class oviparo(mamifero):
    def __init__(self,tipo,mamifero,oviparo):
        self.oviparo = oviparo
        mamifero.__init__(self, tipo, mamifero)
        
