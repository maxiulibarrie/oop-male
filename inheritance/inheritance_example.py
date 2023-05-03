class Animal():

    def is_animal(self):
        return True
    
    def eat(self):
        print(f"{self.name} esta comiendo")

    def run(self):
        pass
    
class Cat(Animal):  

    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} corre como GATO")

class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} corre como PERRO")

#############################

c = Cat("Michi")
d = Dog("Firulais")

# print(f"Michi es un animal: {c.is_animal()}")
# print(f"Firulais es un animal: {d.is_animal()}")

# c.eat()
# d.eat()

animals = [ 
    Cat("Michi"),
    Dog("Firulais"),
    Cat("Antonio"),
    Dog("Ayudante de santa")
]

for a in animals:
    a.run()
    # if a is Cat:
    #     run like Cat
    # else:
    #     run like dog

# Polimorfismo: es que cada objeto sabe como comportarse sin importar el mensaje, solo importa el receptor