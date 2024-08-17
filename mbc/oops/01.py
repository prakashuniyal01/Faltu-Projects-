class Car:
    total_cars = 0
    def __init__(self, brand, model ):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1  # increment the total cars count by 1
        
    def get_brand(self):
        return self.__brand 
        
    def full_name(self):
        return f"{self.__brand} {self.model}"  # f-string formatting
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
        
        
myElectricCar = ElectricCar("tata", "nexon", "60kwh")


print(myElectricCar.full_name() , myElectricCar.battery_size)
    
my_car = Car("toyota" , "corolla")
 
print(my_car.full_name())
print(Car.total_cars)  # accessing the class variable