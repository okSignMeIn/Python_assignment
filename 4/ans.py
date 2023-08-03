import math

class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.length* rectangle.width)