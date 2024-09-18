from bankAccount import min_balance
from checkingAccount import CheckingAccount
from savingAccount import SavingsAccount

timChecking = CheckingAccount("Tim", 1000, min_balance, 100010101, 20010101, 500)
timSaving = SavingsAccount("Tim", 500, min_balance, 100010102, 20010101, 1.01)
gerardChecking = CheckingAccount("Gerard", 1500, min_balance, 100010103, 20010101, 500)
gerardSaving = SavingsAccount("Gerard", 1000, min_balance, 100010104, 20010101, 1.01)

timChecking.withdraw(100)
