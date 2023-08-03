# Method Overloading:
# Method overloading refers to defining multiple methods with the same name but with different parameters or argument lists.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def add(self, num1, num2, num3):
        return num1 + num2 + num3
    
# only latest definition will be considered, first one will throw error, to make that work make the third parameter have a default value

class Calculator:
    def add(self, num1, num2, num3=None):
        if num3 is None:
            return num1 + num2
        else:
            return num1 + num2 + num3

calc = Calculator()
print(calc.add(2, 3))         
print(calc.add(2, 3, 4))       

# Method Overriding:
# Method overriding is a concept where a derived class (subclass) provides a specific implementation for a method that is already defined in its base class (superclass)

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius