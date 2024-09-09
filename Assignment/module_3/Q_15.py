''' Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle '''
import math

class circle:
    def __init__(self,radius) -> None:
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius of the circle: "))

circle = circle(radius)
print(f"The area of the circle is: {circle.area()}")
print(f"The perimeter (circumference) of the circle is: {circle.perimeter()}")
        
