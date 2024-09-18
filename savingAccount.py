from bankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, rate):

        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.rate = rate

    def addInterest(self, interest):
        self.current_balance *= self.rate

