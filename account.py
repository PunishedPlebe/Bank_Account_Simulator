class Account():
    def __init__(self, account_num, account_holder, balance):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("You cannot deposit a zero or negative amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("You cannot withdraw a negative or zero amount")
        else:
            if self.balance <= 0 or amount > self.balance:
                raise Exception("Invalid Withdrawal, You lack the necessary funds.")
            else:
                self.balance -= amount

    def get_balance(self):
        return(self.balance)
