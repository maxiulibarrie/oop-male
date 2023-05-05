class Clothe():
    def __init__(self, tipo, color, talle, precio):
        self.tipo= tipo
        self.color= color
        self.talle= talle
        self.precio= precio 
        
class Shop():
    def __init__(self, fecha, list_clothes=[]):
        self.fecha= fecha
        self.list_clothes= list_clothes
        
    def add_clothe(self, tipo, color, talle, precio):
        new_clothe= Clothe(tipo, color, talle, precio)
        self.list_clothes.append(new_clothe)
    
    def get_total(self):
        
        return sum([c.precio for c in self.list_clothes])