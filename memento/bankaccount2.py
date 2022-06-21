

class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount: 
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount 
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m


    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        if self.current < len(self.changes) - 1:
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(33)
    ba.deposit(10)
    ba.deposit(100)
    print(ba)
    ba.undo()
    print(ba)
    ba.undo()
    print(ba)
    ba.undo()
    print(ba)
    ba.redo()
    print(ba)