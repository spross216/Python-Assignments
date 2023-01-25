#I am not the original author. this is a guided walkthrough to learn OOP concepts

class BankAccount(object):
    defualtAccNumber = 1  #class attribute


    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountnumber = BankAccount.defualtAccNumber
        BankAccount.defualtAccNumber = BankAccount.defualtAccNumber + 1


    def deposit(self, amount):
        self.balance += amount 
    

    def withdrawl(self, amount):
        if self.balance < amount:
            print('Not enough balance')
        else: 
            self.balance -= amount 
    

    def getBalance(self):
        return self.balance


if __name__ == '__main__':
    myObj = BankAccount('Sean', 2500)
    myObj.deposit(1500)
    print(myObj.getBalance())
    myObj.withdrawl(750)
    print(myObj.getBalance())


