#event broker (observer)
#sqs

from abc import ABC
from enum import Enum


class Game:
    def __init__(self) -> None:
        self.queries = Event()

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


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game,'Goblin', 2, 2)
    print(goblin)
    dam = DoubleAttackModifier(game, goblin)
    print(goblin)
    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)