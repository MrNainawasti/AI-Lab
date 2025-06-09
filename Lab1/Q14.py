# Write a Python program to create a class representing a Circle. Include methods to calculate its area
# and perimeter.

import math

PI = math.pi

class Circle:

    def __init__(self, r):
        self.radius = int(r)

    def perimeter(self):
        return 2 * PI * self.radius
    
    def area(self):
        return PI * self.radius**2



radius = input("Enter the radius of circle: ")

circle = Circle(radius)

perimeter = round(circle.perimeter(), 2)
area = round(circle.area(), 2)

print(perimeter, area)