# 1)Create a file with the User classs... + Add a make_withdrawal method

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # def display_user_balance(self):
    #     print(f"{self.name} has {self.account_balance} in their account.") 

    # def transfer_money(self, other_user, amount):


daniel = User("Daniel", "email@fake.com")

daniel.make_deposit(100).make_withdrawal(50)
print(daniel.account_balance)




# 2)Add a display_user_balance method to the User class.

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} in their account.") 
        return self

    # def transfer_money(self, other_user, amount):


daniel = User("Daniel", "email@fake.com")

daniel.make_deposit(100).make_withdrawal(50).display_user_balance()    




# 3)Create 3 instances of the User class + Have the first user make 3 deposits and 1 withdrawal and then display their balance +  Have the second user make 2 deposits and 2 withdrawals and then display their balance + Have the third user make 1 deposits and 3 withdrawals and then display their balance.

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} in their account.") 
        return self

    # def transfer_money(self, other_user, amount):


daniel = User("Daniel", "email@fake.com")
pepper = User("Pepper", "dog@fake.com")
rachel = User("Rachel", "fake@email.com")

daniel.make_deposit(100).make_deposit(1000).make_deposit(200).make_withdrawal(50).display_user_balance()
pepper.make_deposit(50).make_deposit(25).make_withdrawal(10).make_withdrawal(40).display_user_balance()
rachel.make_deposit(1000).make_withdrawal(10).make_withdrawal(100).make_withdrawal(500).display_user_balance()




# Bonus) Add a transfer_money method; have the first user transfer money to the third user, and then print both user's balances

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has {self.account_balance} in their account.") 
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


daniel = User("Daniel", "email@fake.com")
pepper = User("Pepper", "dog@fake.com")
rachel = User("Rachel", "fake@email.com")

daniel.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance().transfer_money(rachel, 10)
print('Daniel and Rachel balance below!')
daniel.display_user_balance()
rachel.display_user_balance()


