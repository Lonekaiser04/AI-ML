class Account:
    def __init__(self,amount):
        self.amount = amount
        self.balance = 1000
        self.acc_no = 2106
    def debit(self):
        if self.amount <= self.balance:
            self.balance-=self.amount
            print(f"available balance ={self.balance}")
        else:
            print("Insufficient balance")    
    def cridit(self):
        self.balance+=self.amount
        print(f"{self.amount} creidicted in your account")
        print(f"Available balance = {self.balance}")
    def display(Self):
        print(f"Total balance in your account ={Self.balance}")

while True:
    user = int(input("Enter\n1.Cridit\n2.Debit\n3.Check balance\n4.Exit\nEnter your Choice:"))
    if user == 1:
        amount = int(input("Enter amount to deposit:"))
        person1 = Account(amount)
        person1.cridit()
    elif user == 2:
        amount = int(input("Enter amount to Withdraw:"))
        person1 = Account(amount)
        person1.debit()
    elif user == 3:
        person1 = Account(1)
        person1.display()
    elif user == 4:
        print("Exiting...Thank you!")
        break
    else:
        print("Enter valid choice...")




