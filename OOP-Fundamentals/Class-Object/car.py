class Car:
    #constructor
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    def accelerate(self, increment):
        self.__speed += increment
    
    def decelerate(self, decrement):
        self.__speed -= decrement
    
    def speedometer(self):
        return self.__speed
    
    def status(self):
        print(self.__brand, self.__model, self.__year)

if __name__ == "__main__":
    car1 = Car("Remac", "Nevara", "2024")
    car1.accelerate(300)
    car1.accelerate(300)
    car1.accelerate(300)
    print(car1.speedometer())
    car1.status()

    
    