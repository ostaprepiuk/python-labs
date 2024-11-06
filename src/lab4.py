class Car:

    def __init__(self, brand="Nissan Skyline", power=320, speed=260, color="White", year=5):
        self.__brand = brand
        self.__power = power
        self.__speed = speed
        self.color = color
        self.year = year
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__car_brand = brand
    
    def get_power(self):
        return self.__power
    
    def set_power(self, power):
        self.__car_power = power
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__car_speed = speed

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def __repr__(self):
        return f"car(Brand = {self.__brand}, Power = {self.__power}HP, Max Speed = {self.__speed}km/h, Year: {Car.year})"
    
    def __str__(self):
        return f"Brand: {self.__brand}, Power: {self.__power}HP, Max Speed: {self.__speed}km/h, Year: {Car.year}"
    
    def __del__(self):
        print("Car deleted")

def main():
    car0 = Car()
    car1 = Car("Toyota Supra", 330, 280)
    car2 = Car("Mazda RX-7", 236, 250)
    car3 = Car("Lexus LFA", 560, 325)
    print(car0)
    print(car1)
    print(car2)
    print(repr(car3))

if __name__ == "__main__":
    main()
