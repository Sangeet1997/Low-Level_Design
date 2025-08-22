from enum import Enum

class Coins(Enum):
    PENNY = 1
    NICKLE = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self.coin_value = value
    
    def get_value(self):
        return self.coin_value

if __name__ == "__main__":
    coin1 = Coins.PENNY
    coin2 = Coins.DIME
    print(coin1.get_value() + coin2.get_value())