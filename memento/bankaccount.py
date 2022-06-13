

class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount: 
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(33)
    m1 = ba.deposit(10)
    m2 = ba.deposit(100)
    print(ba)
    ba.restore(m1)
    print(ba)
    ba.restore(m2)
    print(ba)