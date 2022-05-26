
"""
Дан проект игры с классами Goblin и GoblinKing. Реализуйте следующие правила:

У goblin базовые характеристики 1 атака / 1 защита (1/1), у goblin king 3/3
Когда goblin king в игре, все остальные гоблины получают +1 к атаке
Гоблины получают +1 к защите за каждого другого гоблина в игре (goblin king - тоже гоблин!)

Например:
Есть 3 гоблина в игре. Тогда у каждого следующие характеристики - 1/3 (1/1 базово + 0/2 бонус к защите)
В игру приходит goblin king.
Теперь характеристики каждого гоблина 2/4 (1/1 + 0/3 бонус к защите от "друзей-гоблинов" + 1/0 к атаке от goblin king)

Состояние всех гоблинов в каждый момент времени должно быть непротиворечиво.
"""

from abc import ABC
from enum import Enum
import unittest

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        # todo
        pass

class GoblinKing(Goblin):
    def __init__(self, game):
        # todo
        pass

class Game:
    def __init__(self):
        self.creatures = []



class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)