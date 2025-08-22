class bankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt
    
    def withdraw(self, amt):
        if amt > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amt
    
    def checkBalance(self):
        return self.__balance

class PaymentProcessor:
    def __init__(self, arr):
        self.__card_num = arr
        self.__bankAcc = bankAccount()
    
    def deposit(self, amt):
        self.__bankAcc.deposit(amt)
        print("Deposited to Bank account with card number: **** ", self.__card_num[-4:])

    def withdraw(self, amt):
        self.__bankAcc.withdraw(amt)
        print("Withdraw successful from Bank account with card number: **** ", self.__card_num[-4:])

    def show_balance(self):
        return self.__bankAcc.checkBalance()
        
if __name__=="__main__":
    card_numbers = [
    [4, 5, 3, 9, 8, 7, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
    ]
    process1 = PaymentProcessor(card_numbers[0])
    process2 = PaymentProcessor(card_numbers[1])

    process1.deposit(5000)
    process2.deposit(10000)
    process1.withdraw(999)
    process1.deposit(14000)
    process2.withdraw(333)

    print(process1.show_balance())
    print(process2.show_balance())
