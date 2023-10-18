from main import BankAccount

class NewBankAccount(BankAccount):
    def __init__(self, account_number: int, owner_name: str, balance: int, currency: str, max_limit: int, max_count_transactions=5):
        super().__init__(account_number, owner_name, balance, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.i = 0

    def transfer(self, to_acc, money):
        if money < self.max_limit and self.i <= self.max_count_transactions:
            self.i += 1
            return super().transfer(to_acc, money)
        else:
            print("Перевищено максимальний ліміт операції або к-сть спроб!")

    def withdraw(self, money):
        if money < self.max_limit and self.i <= self.max_count_transactions:
            self.i += 1
            return super().withdraw(money)
        else:
            print("Перевищено максимальний ліміт операції або к-сть спроб!")

    def add_money(self, percent):
        self.deposit(self.balance.amount * (percent / 100))


if __name__ == '__main__':
    acc1 = NewBankAccount(64547, "Slavik", 15000, 'USD', 7500)
    acc2 = NewBankAccount(9834, "Miroslav", 25000, 'EUR', 12500, 3)

    acc1.withdraw(3000)
    print(acc1)
    print()

    acc2.withdraw(100)
    print(acc2)
    print()

    acc1.transfer(acc2, 499)
    print(acc1)
    print()

    acc2.add_money(15)
    print(acc2)
