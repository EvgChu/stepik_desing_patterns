"""
    В системе может быть любое количество экземпляров класса Participant.
    Каждый экземпляр имеет целочисленный атрибут value изначально инициализируемый 
нулём.

    Экземпляр participant может сказать say(), выдав значение, транслируя 
его всем участникам.
    В данной точке во времени каждый участник обязан увеличить своё собственное 
значение на транслированное значение.

Пример:

Два участника начинают со значений 0 соответственно
  - Участник 1 транслирует значение 3. 
    Теперь у нас Participant 1 value = 0, Participant 2 value = 3
  - Участник 2 транслирует значение 2. 
    Теперь у нас Participant 1 value = 2, Participant 2 value = 3
"""
import unittest


class Mediator:
    def __init__(self) -> None:
        self.participants = []

    def join(self, participant):
        self.participants.append(participant)

    def broadcast(self, source, message):
        for p in self.participants:
            if p is not source:
                p.receive(message)

class Participant:
    def __init__(self, mediator: Mediator):
        self.value = 0
        self.mediator = mediator
        mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)

    def receive(self, value):
        self.value += value


class TestMediator(unittest.TestCase):
    def test_main(self):
        x = 2
        y = 3
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)
        result = f'{p1.value} {p2.value} '
        p1.say(int(x))
        result += f'{p1.value} {p2.value} '
        p2.say(int(y))
        result += f'{p1.value} {p2.value}'
        self.assertEqual('0 0 0 2 3 2', result)



if __name__ == "__main__":
    unittest.main()

