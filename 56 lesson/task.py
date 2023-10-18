from new_bank import NewBankAccount


class UpBankAccount(NewBankAccount):

    def __init__(self, account_number: int, owner_name: str, balance: int, currency: str, max_limit: int,
                 max_count_transactions=5):
        super().__init__(account_number, owner_name, balance, currency, max_limit, max_count_transactions)

    def __eq__(self, other):
        if self.balance.currency == other.balance.currency:
            return True
        else:
            return False

    def __bool__(self):
        if self.balance.amount > 0:
            return True
        return False

    def __add__(self, other: int):
        self.deposit(other)
        return id(self)

    def __sub__(self, other: int):
        self.withdraw(other)
        return id(self)

    def __call__(self, value=0):
        if value == 0:
            print(f"Баланс: {self.balance.amount}")
        if value > 0:
            self.deposit(value)
            print(f"Баланс було поповнено на суму {value} {self.balance.currency}")
        if value < 0:
            self.withdraw(value)
            print(f"З балансу було списано {value} {self.balance.currency}")

    def __setattr__(self, name, value):
        # print(f"Грошей на балансі було: {self.balance.amount}")
        self.__dict__[name] = value
        # print(f"Грошей на балансі стало: {self.balance.amount}")


if __name__ == '__main__':
    acc1 = UpBankAccount(64547, "Slavik", 15000, 'USD', 7500)
    acc2 = UpBankAccount(9834, "Oleh", -25000, 'EUR', 12500, 3)

    print(acc1.balance.amount)
    print(acc2.balance.amount)
    print()

    print(bool(acc1))
    print(bool(acc2))
    print()

    print(acc1 + 4000)
    print(acc1 - 4000)
    print()

    acc1()
    acc1(0)
    acc1(20000)
    acc1(-1000)
    print()

    acc2.balance.amount = -100000
    print(acc2.balance.amount, acc2.balance.currency)
