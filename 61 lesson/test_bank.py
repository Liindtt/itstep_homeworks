from unittest import TestCase
from bank import BankAccount


class MainTest(TestCase):

    def setUp(self):
        self.obj_account = BankAccount(64547, "Slavik", 15000, 'USD')
        self.obj_account2 = BankAccount(9834, "Miroslav", 25000, 'EUR')

    def tearDown(self):
        del self.obj_account

    def test_deposit(self):
        self.obj_account.deposit(1000)
        self.assertEqual(self.obj_account.balance.amount, 16000)

    def test_withdraw(self):
        self.obj_account.withdraw(500)
        self.assertEqual(self.obj_account.balance.amount, 14500)

    def test_change_owner_name(self):
        self.obj_account.change_owner_name("Volodymyr")
        self.assertEqual(self.obj_account.owner_name, "Volodymyr")

    def test_transfer(self):
        self.obj_account2.transfer(self.obj_account, 10000)
        self.assertEqual(self.obj_account.balance.amount, 25000)
        self.assertEqual(self.obj_account2.balance.amount, 15000)

    def test_check_account_number(self):
        self.assertFalse(self.obj_account2.check_account_number(self.obj_account2.account_number))

    def test_set_account_number(self):
        self.obj_account2.set_account_number(88005353535)
        self.assertEqual(self.obj_account2.account_number, 88005353535)

    def test_get_account_number(self):
        self.assertTrue(self.obj_account2.get_account_number(), 88005353535)

