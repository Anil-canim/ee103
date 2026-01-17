class ElectronicsDevices(object):
    def __init__(self, brand, model, power_status=False):
        self.brand = brand          # String: Brand of the device
        self.model = model          # String: Model of the device
        self.power_status = power_status  # Boolean: Power status (On/Off)

    def power_on(self):
        self.power_status = True
        return f"{self.brand} {self.model} is now ON."
    
    def power_off(self):
        self.power_status = False
        return f"{self.brand} {self.model} is now OFF."
    
    def is_powered_on(self):
        return self.power_status
    def device_info(self):
        return f"Device Info: Brand - {self.brand}, Model - {self.model}, Power Status - {'On' if self.power_status else 'Off'}"
    
class calculator(ElectronicsDevices):
    def __init__(self, brand, model, power_status=False):
        super().__init__(brand, model, power_status)
    
        if self.power_status!=True:
            print("Please power on the calculator to use its functions.")
        else:
            pass
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
class listoscopes(ElectronicsDevices):
    def __init__(self, brand, model, power_status=False):
        super().__init__(brand, model, power_status)

    def measure_length(self, list_input):
        return len(list_input)
    
class Fraction(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator      # Integer: Numerator of the fraction
        self.denominator = denominator  # Integer: Denominator of the fraction

    def simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        common_divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self

    def add(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only add another Fraction.")
        
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator).simplify()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"