# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

#1)   deposit(self, amount) - increases the account balance by the given amount
#2)   withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#3)   display_account_info(self) - print to the console: eg. "Balance: $100"
#4)   yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)


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


Account1 = BankAccount(1000, 0.10)
Account2 = BankAccount(500, 0.20)

Account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
Account2.deposit(200).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

