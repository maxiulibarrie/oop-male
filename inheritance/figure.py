class Figure():

    def is_figure():
        return True
    
class Square(Figure):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class Circle(Figure):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * ( self.radio ** 2 )

#################################
# MAIN

figures = [
    Square(3),
    Circle(2),
    Square(1),
    Circle(5)
]

for f in figures:
    print( f.area() )
    # if f is Square
    #     return side ** 2
    # else:
    #     pi * radio **2