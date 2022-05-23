
class CEO:
    __shared_state = {
        'name': "Steve",
        'age': 77
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years'


class Monostate:
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ""
        self.money_manage = 0

    def __str__(self) -> str:
        return f'{self.name} is {self.money_manage}'

if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.age = 22
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = "Test"
    cfo1.money_manage = 2
    print(ceo1)
    cfo2 = CFO()
    cfo1.name = "Second"
    cfo1.money_manage = 1
    print(cfo1)
    print(cfo2)