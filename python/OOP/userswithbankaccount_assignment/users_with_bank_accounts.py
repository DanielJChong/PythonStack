class BankAccount:
    def __init__(self, balance, int_rate):
        self.int_rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self


class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):	
        self.account.deposit(amount)
        print(self.account.account_balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.account_balance)
        return self

    def display_user_balance(self):
        self.account.display_account_info
        return self


daniel = User("Daniel", "email@fake.com")
rachel = User("Rachel", "fake@email.com")
pepper = User("Pepper", "dog@fake.com")

daniel.make_deposit(1000).make_withdrawal(50).display_user_balance()
