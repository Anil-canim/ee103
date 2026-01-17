# Write the class according to the specifications below:
import math
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius=radius
    def get_radius(self):
        """ Returns the radius of self """
        return self.radius
    def set_radius(self, radius):
        """ radius is a number
    Changes the radius of self to radius """
        self.radius=radius
    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return math.pi*(self.radius**2)
    def equal(self, c):
        """ c is a Circle object
    Returns True if self and c have the same radius value """
        return self.radius==c.radius

    def bigger(self, c):
        """ c is a Circle object
    Returns self or c, the Circle object with the bigger radius """
        
    # your code here
        if self.radius>c.radius:
            return self
        else:
            return c
    def __add__(self, other_circle):
       
        third_radius= self.radius + other_circle.radius
        return Circle(third_radius)
    def __str__(self):
        """
        print(circle_objesi) denildiğinde çalışır.
        """
        return f"Circle object with radius: {self.radius}"
    1 # your class here


circle1=Circle(5)
circle2=Circle(4)
print((circle1.bigger(circle2)).get_area())
circle1+circle2
print((circle1+circle2).get_area())
print(f'{circle1} | {circle2} | {circle1+circle2}')
print("-----END OF THIS CALCULATION-----")