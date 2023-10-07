import requests
import os
import json

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

class BankAccount:

    __exchange_rate = {}
    accounts = []

    def __init__(self, account_number: int, owner_name: str, balance: int, currency):
        self.__account_number = account_number
        self.owner_name = owner_name
        self.balance = Money(balance, currency)
        self.accounts.append(self)

    def __str__(self):
        return f"Номер рахунку: {self.__account_number}\nБаланс: {self.balance}$"

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def change_owner_name(self, new_name: str):
        self.owner_name = new_name

    def display_account_info(self):
        print(f"Номер рахунку: №{self.__account_number}\nІм\'я власника: {self.owner_name}\nБаланс: {self.balance}")

    def transfer(self, to_acc, money):
        print(f"Поточний баланс: {self.balance}")
        try:
            if self.balance < money:
                raise ValueError("У вас недостатьо грошей на балансі!")
        except ValueError as error:
            print(f"Помилка: {error}")
            return False

        try:
            if money < 0:
                raise ValueError("Введена некоректна сума")

            self.balance -= money
            to_acc.deposit(money)
            print(f"Оновлений баланс: {self.balance}")

        except ValueError as error:
            print(f"Помилка: {error}")

    @staticmethod
    def check_account_number(check_acc_num: int):
        if len(str(check_acc_num)) == 5:
            print("Номер рахунку валідний!")
        else:
            print("Номер рахунку не валідний!")

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, new_acc_num):
        if len(str(new_acc_num)) == 5:
            self.__account_number = new_acc_num
        else:
            raise ValueError("Некорректно введений номер рахунку!")

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_acc_num):
        if len(str(new_acc_num)) == 5:
            self.__account_number = new_acc_num
        else:
            raise ValueError("Некорректно введений номер рахунку!")

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance.amount
        return total / len(cls.accounts)

    @classmethod
    def create_exchange_rate(cls):
        try:
            response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
            data = response.json()
            for currency_data in data:
                currency_code = currency_data["cc"]
                exchange_rate = currency_data["rate"]
                cls.__exchange_rate[currency_code] = exchange_rate
        except Exception as e:
            print(f"Помилка при завантаженні курсів обміну: {e}")

    def save_to_file(self):
        filename = f'data/{self.account_number}.json'
        os.makedirs('data', exist_ok=True)
        with open(filename, "w") as file:
            data = {
                "account_number": self.account_number,
                "balance": self.balance.amount,
                "owner_name": self.owner_name,
                "currency": self.balance.currency
            }
            json.dump(data, file, indent=4)

    def transfer_funds(self, target_account, amount):
        if 0 < amount <= self.balance.amount:
            source_currency = self.balance.currency
            target_currency = target_account.balance.currency
            if source_currency == target_currency:
                self.balance.amount -= amount
                target_account.deposit(amount)
            elif source_currency in BankAccount.__exchange_rate and target_currency in BankAccount.__exchange_rate:
                source_rate = BankAccount.__exchange_rate[source_currency]
                target_rate = BankAccount.__exchange_rate[target_currency]
                converted_amount = amount / source_rate * target_rate
                self.balance.amount -= amount
                target_account.deposit(converted_amount)
            else:
                print("Неможливо конвертувати валюту")


acc1 = BankAccount(64547, "Slavik", 15000, 'USD')
acc2 = BankAccount(9834, "Miroslav", 25000, 'EUR')

matching_accounts = BankAccount.find_accounts_by_owner("Slavik")
for account in matching_accounts:
    account.display_account_info()

print(f"Середній баланс коштів усіх користувачів: {BankAccount.get_average_balance()}")

acc1.transfer_funds(acc2, 300)
print(acc1.display_account_info())
print(acc2.display_account_info())
