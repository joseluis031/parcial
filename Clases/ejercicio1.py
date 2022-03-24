class libro:
    def __init__(self,autor,genero,isbn):
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
    
    def get_autor(self):
        return self.autor
    
    def get_genero(self):
        return self.genero
    
    def get_isbn(self):
        return self.isbn
    
final = libro("jose","aventuras",92248)
print ("El autor del libro es:",final.get_autor(),".El genero del libro es: ",final.get_genero(),".El isbn del libro es: ",final.get_isbn())