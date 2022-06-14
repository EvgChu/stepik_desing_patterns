"""
    Представьте себе игру, в которой одна или более крыс (rats) могут атаковать
игрока (player). У каждой крысы в отдельности атака = 1. Однако, крысы могут
образовывать рой, и, тогда атака каждой крысы становится равной количеству всех
крыс в игре.

    Крыса добавляется в игру посредством инициализации объекта Rat, а умирает
через метод __exit__.

    Реализуйте классы Game и Rat таким образом, чтобы значение атаки у крыс
в любой момент времени было корректно и непротиворечиво.
"""

import unittest



class Game:
    def __init__(self):
        self.rats = []

    def join(self, rat):
        self.rats.append(rat)
        for r in self.rats:
            r.set_attack(len(self.rats))

    def exit(self, rat):
        self.rats.remove(rat)
        for r in self.rats:
            r.set_attack(len(self.rats))

class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack = 1
        self.game.join(self)

    def set_attack(self, value):
        self.attack = value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.game.exit(self)


class TestGame(unittest.TestCase):
    def test_three_rats_one_dies(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)
        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

if __name__ == "__main__":
    unittest.main()