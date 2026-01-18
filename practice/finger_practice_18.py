class Circle():
    def __init__(self, radius,name="unnamed circle"):
        """ Initializes self with radius """
        self.radius=radius
        self.name=name
    def get_radius(self):
        """ Returns the radius of self """
        return self.radius
    def __add__(self, circle):
        """ c is a Circle object
        Returns a new Circle object whose radius is
        the sum of self and c's radius """
        new_radius=self.radius+circle.radius
        return Circle(new_radius,"combined circle")
    def __str__(self):
        """ A Circle's string representation is the radius """
        return f"{self.radius} is the radius of the {self.name}"
    # your code here

circle1=Circle(15,"circle-1")
circle2=Circle(8,"circle-2")
circle3=circle1+circle2
print(circle3,"|",circle2,"|",circle1)