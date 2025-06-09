# Implement   a   class  Shape  with   a   method  area()  which   returns   0.   Then,   create   subclasses
# Rectangle  and  Circle. Overload the  area()  method in both subclasses to calculate and return
# the area of a rectangle and a circle respectively.

import math  


class Shape:
    
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2


# Create a Shape object
shape = Shape()
print(f"Default area (Shape): {shape.area()}")  

# Create a Rectangle object
rectangle = Rectangle(5, 10)
print(f"Area of Rectangle: {rectangle.area()}") 

# Create a Circle object
circle = Circle(7)
print(f"Area of Circle: {circle.area():.2f}")  
