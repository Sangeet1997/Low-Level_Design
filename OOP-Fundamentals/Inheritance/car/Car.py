class Car:
    def __init__(self):
        self.engineRunning = False
    
    def startEngine(self):
        if self.engineRunning:
            raise ValueError("Already Running.")
        else:
            print("Starting Car...")
            self.engineRunning = True

    def stopEngine(self):
        if not self.engineRunning:
            raise ValueError("Engine was already off")
        else:
            print("Stopping Car...")
            self.engineRunning = False
    
class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def chargeBattery(self):
        print("Charging battery")
    
class GasCar(Car):
    def __init_(self):
        super.__init__()

    def fillTank(self):
        print("Filling Tank")

if __name__ == "__main__":
    car1 = ElectricCar()
    car2 = GasCar()
    try:
        car1.startEngine()
        car1.stopEngine()
        car1.chargeBattery()
        print()
        car2.startEngine()
        car2.stopEngine()
        car2.fillTank()
        car2.stopEngine()
    except ValueError as e:
        print(e)
    