bank = "Big Bank"
min_balance = 0.01

class BankAccount():

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount
        return "Your new balance is: " + str(self.current_balance)

    def withdraw(self, withdrawal_amount):
        if self.current_balance >= self.minimum_balance:
            self.current_balance -= withdrawal_amount
            return "Your new balance is: " + str(self.current_balance)
        else:
            return "Sorry, you have an insufficient balance"

    def print_customer_information(self):
        print(bank + " Account Holder: " + self.customer_name + ", Current Balance: " + str(self.current_balance) + ", Minimum Balance: " + str(self.minimum_balance))

sammy = BankAccount("Sammy", 1000, min_balance)
roberto = BankAccount("Roberto", 50, min_balance)

sammy.print_customer_information()
print(sammy.withdraw(1000))
print(sammy.withdraw(500))
print(sammy.deposit(500))
sammy.print_customer_information()