class animal:
    def __init__(self, tipo):
        self.tipo = tipo
        
class mamifero(animal): #utilizo la herencia multiple
    def __init__(self,tipo,mamiferoo):
        self.mamiferoo = mamiferoo
        animal.__init__(self, tipo)
        
class oviparo(mamifero,animal):
    def __init__(self,tipo,mamiferoo,oviparo):
        self.oviparo = oviparo
        mamifero.__init__(self, tipo, mamiferoo)


pollo =
gato =
ornitorrinco =
print(pollo.animal)
print(gato.mamifero)
print(ornitorrinco.oviparo)
