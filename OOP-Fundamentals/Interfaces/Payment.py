from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass
    
class ChaseGateway(PaymentGateway):
    def initiate_payment(self, amount):
        print("Chase gateway:", amount)

class BofaGateway(PaymentGateway):
    def initiate_payment(self, amount):
        print("Bofa gateway:", amount)

if __name__ == "__main__":
    payment1 = ChaseGateway()
    payment2 = BofaGateway()

    payment1.initiate_payment(3000)
    payment2.initiate_payment(2000)

