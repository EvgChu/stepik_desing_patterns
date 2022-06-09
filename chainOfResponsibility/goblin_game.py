
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


class Game:
    def __init__(self) -> None:
        self.queries = Event()
        self.creatures = []

    def perfome_query(self, sender, query):
        self.queries(sender, query)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sendr, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and\
            query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2

class JoinDefenderModifier(CreatureModifier):
    def handle(self, sender, query):
        if (isinstance(sender, Goblin) and sender is not self.creature and
            query.what_to_query == WhatToQuery.DEFENSE):
            query.value += 1

class KingAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (isinstance(sender, Goblin) and sender is not self.creature and
            query.what_to_query == WhatToQuery.ATTACK):
            query.value += 1


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE,
                    self.initial_defense)
        self.game.perfome_query(self, q)
        return q.value

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK,
                    self.initial_attack)
        self.game.perfome_query(self, q)
        return q.value

    def __str__(self) -> str:
        return f'{self.name} ({self.attack}/{self.defense})'

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, "goblin", attack, defense)
        JoinDefenderModifier(game, self)

class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)
        KingAttackModifier(game, self)


class FirstTestSuite(unittest.TestCase):
    def test_goblin(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
        goblin2 = Goblin(game)
        game.creatures.append(goblin2)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

    def test_kinggoblin(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
        goblin2 = GoblinKing(game)
        game.creatures.append(goblin2)
        self.assertEqual(2, goblin.attack)
        self.assertEqual(2, goblin.defense)


if __name__ == "__main__":
    unittest.main()
    