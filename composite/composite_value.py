import unittest
from abc import ABC
from collections.abc import Iterable

class Summable(ABC, Iterable):
    @property
    def sum(self):
        result = 0
        for value in self:
            if isinstance(value, Summable):
                result += value.sum
            else:
                result += value
        return result

class SingleValue(Summable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value 

class ManyValues(list, Summable):
    pass


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)

        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)

        self.assertEqual(all_values.sum, 66)


if __name__ == "__main__":
    unittest.main()
    