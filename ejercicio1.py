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
    
final = libro ("jose","aventuras",92248)
print (final.get_autor,final.get_genero,final.get_isbn)