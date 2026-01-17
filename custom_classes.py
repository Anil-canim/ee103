from electronics_devices import *

ElectronicsDevice1=ElectronicsDevices("Samsung", "Galaxy S21", True)
ElectronicsDevice2=ElectronicsDevices("Apple", "iPhone 13", False)
print(ElectronicsDevice1.device_info())
print(ElectronicsDevice2.power_on())
print(ElectronicsDevice1.is_powered_on())

calc1=calculator("Casio","FX-991EX",False)
print(calc1.device_info())

print("Addition:", calc1.add(5,3))
print("Subtraction:", calc1.subtract(10,4))

print(listoscopes("Tektronix","TBS1052B",True).measure_length([1,2,3,4,5]))