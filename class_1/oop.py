"""
- imperativa (secuencial, condicional, iterativa) - funciones y procedimientos
- funcional 
- orientación a objetos

Para la OOP:
* un sistema es una colaboración entre objetos.
* encapsulamiento y abstracción
* abstracción significa: no importa el COMO sino el QUE
* instancia == objeto
"""

## empieza definición de clase Product
class Product():

    def __init__(self, description, price):
        # atributos
        self.description = description
        self.price = price

    # metodo (instancia) 
    def increment_price_15(self):
        self.price = self.price * (1 + 0.15)
## termina definición de clase Product

if __name__=='__main__':
    ## objeto 
    product0 = Product("Yerba", 500)

    print(f"Descripción del producto: {product0.description}")
    print(f"Precio del producto: {product0.price}")
    print(f"Tipo del objeto producto: {type(product0)}")
    print("#######################")
    print("Incrementamos un 15%")
    product0.increment_price_15()

    print(f"Precio nuevo del producto: {product0.price}")
