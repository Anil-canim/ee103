# Question 1:
# Write a class definition for a vehicle. A vehicle is defined by attributes:
# Number of wheels
# Number of occupants
# Color 
# Decide the type of each data attribute and document this

        
class vehicle:
    def __init__(self, wheels, occupants,color):
        self.max_occup=5
        self.color=color
        self.wheels=wheels
        self.occupants=occupants
    def add_n_occupants(self,n):
        
        if self.occupants+n >self.max_occup:
            raise ValueError("out of capacity")
        self.occupants+=n
        return self.occupants
vehicle1= vehicle(2,1,"red")
vehicle2= vehicle(18,3,"green")
print(vehicle1.occupants)
print(vehicle2.color)
print(vehicle2.add_n_occupants(2))
print(vehicle2.add_n_occupants(7))



# Question 2:
# Create 2 vehicle instances using the class we wrote previously. 
# One red vehicle with 2 wheels, and 1 occupant
# One green vehicle with 18 wheels, and 3 occupants
# Print the first one's number of occupants
# Print the second one's color

# Question 3:
# Add on to the code from above for class Vehicle.
# Create another method for the vehicle class named add_n_occupants, 
# which takes in an int n. When called, self's number of occupants 
# increases by n. It returns the total occupants after the increase. 

# Question 4:
# Add another data attribute to the Vehicle class, called max_occupancy,
# which is always 5. This attribute is not passed in as a parameter, but 
# is defined in the init.
# Modify the add_n_occupants methods such that if adding the occupants 
# exceeds the max_occupancy allowed for that vehicle, 
#   * you do not perform the increase, and
#   * you raise a ValueError with an apprpriate message