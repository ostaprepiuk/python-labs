class car:
    def __init__(self, Brand = "Nissan", Power = 320, Speed = 260):
        self.car_Brand = Brand
        self.car_Power = Power
        self.car_Speed = Speed
        
    def get_brand(self):
        return self.car_Brand
    
    def get_power(self):
        return self.car_Power
    
    def get_speed(self):
        return self.car_Speed
    
    def __repr__(self):
        return f"car(Brand = {self.car_Brand}, Power = {self.car_Power}, Max Speed = {self.car_Speed})"
    
    def __str__(self):
        return f"Brand:{self.car_Brand}, Power:{self.car_Power}, Max Speed:{self.car_Speed}"
    
car1 = car("Toyota", "330HP", "280km/h")
car2 = car("Mazda", "236HP", "250km/h")
car3 = car("Lexus", "560HP", "325km/h")
print(car1)
print(repr(car1))
print(car2)
print(repr(car2))
print(car3)
print(repr(car3))