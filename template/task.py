'''
    Представьте себе типичную коллекционную карточную игру, в которой карты
представляют существ.
    У каждого существа есть два атрибута: атака (attack) и здоровье (health).
Существа могут сражаться, нанося урон равный значению атаки (уменьшая здоровье
существа на которое совершена атака).

    Класс CardGame реализует логику для двух сражающихся существ.
Однако, конкретная механика нанесения урона может меняться:

    TemporaryCardDamage : в некоторых играх (например Magic: the Gathering),
пока существо не уничтожен, его здоровье восстанавливается то исходного уровня
в конце каждого сражения (combat)

    PermanentCardDamage : в других играх (e.g., Hearthstone), нанесённый
урон сохраняется.

    Реализуйте классы TemporaryCardDamageGame и PermanentCardDamageGame которые
реализуют описанную логику.

    Пара примеров:

    - В режиме временного урона два существа с характеристикам 1/2 и 1/3 никогда
друг друга убить не смогут.
    - В режиме постоянного урона, второе существо победит через два раунда

    - В любом из двух режимах два существа с характеристиками 2/2 убьют друг друга
'''


import unittest
from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        if c1_index >= len( self.creatures) or c2_index >= len( self.creatures):
            return -1
        if self.creatures[c1_index].health <= 0 and self.creatures[c2_index].health > 0:
            return c2_index
        if self.creatures[c2_index].health <= 0 and self.creatures[c1_index].health > 0:
            return c1_index
        p1, p2 = self.hit(self.creatures[c1_index], self.creatures[c2_index])
        if p1 <= 0 and p2 > 0:
            return c2_index
        if p2 <= 0 and p1 > 0:
            return c1_index
        return -1

    def hit(self, attacker: Creature, defender: Creature) -> int:
        raise NotImplemented  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature) -> int:
        points1 = defender.health - attacker.attack
        points2 = attacker.health - defender.attack
        return points1, points2

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature) -> int:
        defender.health = defender.health - attacker.attack
        attacker.health = attacker.health - defender.attack
        defender.health = defender.health if defender.health >= 0 else 0
        attacker.health = attacker.health if attacker.health >= 0 else 0
        return attacker.health, defender.health

class FirstTestSuite(unittest.TestCase):
    def test_temporary(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)

        game = TemporaryDamageCardGame([c1, c2])
        res1 = game.combat(0, 1)
        result = f'Temporary strategy:{res1} Creature1.Health={c1.health} Creature2.Health={c2.health} '
        res2 = game.combat(0, 1)
        result += f'{res2} Creature1.Health={c1.health} Creature2.Health={c2.health}.'
        self.assertEqual(
            "Temporary strategy:-1 Creature1.Health=2 Creature2.Health=2 -1 Creature1.Health=2 Creature2.Health=2.",
            result
        )
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)

    def test_permanent(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = PermanentDamageCardGame([c1, c2])
        res1 = game.combat(0, 1)
        result = f'Permanent strategy:{res1} Creature1.Health={c1.health} Creature2.Health={c2.health} '
        res2 = game.combat(0, 1)
        result += f'{res2} Creature1.Health={c1.health} Creature2.Health={c2.health}'
        self.assertEqual(
            "Permanent strategy:-1 Creature1.Health=1 Creature2.Health=1 -1 Creature1.Health=0 Creature2.Health=0",
            result
        )

    def test_permanent_win2(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        res1 = game.combat(0, 1)
        self.assertEqual(res1, -1)
        self.assertEqual(c1.health, 1)
        self.assertEqual(c2.health, 2)
        res2 = game.combat(0, 1)
        self.assertEqual(res2, 1)
        self.assertEqual(c1.health, 0)
        self.assertEqual(c2.health, 1)

    def test_permanent_wrong2(self):
        c1 = Creature(1, 1)
        c2 = Creature(1, 2)
        game = PermanentDamageCardGame([c1, c2])
        res1 = game.combat(0, 1)
        self.assertEqual(res1, 1)
        self.assertEqual(c1.health, 0)
        self.assertEqual(c2.health, 1)
        res2 = game.combat(0, 1)
        self.assertEqual(res2, 1)
        self.assertEqual(c1.health, 0)
        self.assertEqual(c2.health, 1)

if __name__ == "__main__":
    unittest.main()