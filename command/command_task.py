import unittest

from enum import Enum

"""
Реализуйте Account.process() метод для обработки различных команд, связанных с аккаунтом.
Правила просты:
флаг success обозначает успешность операции
чтобы снять сумму денег, она должна быть на счёте
"""

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command: Command):
        if command.action == command.Action.DEPOSIT:
            self.deposit(command.amount)
            command.success = True
        elif command.action == command.Action.WITHDRAW:
            command.success = self.withdraw(command.amount)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return True
        return False


class TestSuite(unittest.TestCase):
    def test_account(self):
        a = Account()
        cmd = Command(Command.Action.DEPOSIT, 100)
        a.process(cmd)
        self.assertEqual(100, a.balance)
        self.assertEqual(True, cmd.success)
        cmd = Command(Command.Action.WITHDRAW, 50)
        a.process(cmd)
        self.assertEqual(50, a.balance)
        self.assertEqual(True, cmd.success)
        cmd = Command(Command.Action.WITHDRAW, 150)
        a.process(cmd)
        self.assertEqual(50, a.balance)
        self.assertEqual(False, cmd.success)


if __name__ == "__main__":
    unittest.main()



