class BankAccount:

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


account = BankAccount(4441, 10000)

account.set_balance(12000)
print(account.get_balance())
account.set_account_number(4444)
print(account.get_account_number())


