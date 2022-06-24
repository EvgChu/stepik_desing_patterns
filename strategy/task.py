"""
Рассмотрим квадратное уравнение и его каноническое решение:

    Часть b^2-4*a*c называется дискриминантом. Предположим, что мы хотим 
предоставить два API с разными стратегиями вычисления дискриминанта.

    В стратегии OrdinaryDiscriminantStrategy , если дискриминант < 0, его
так и возвращаем. Это нормально, потому что основной API так или иначе
возвращает пару комплексных чисел.

    В стратегии RealDiscriminantStrategy ,  если дискриминант < 0,
то надо возвращать NaN (not a number). NaN проходит через вычисления,
и solver даёт два NaN значения. В Python, вы можете создать такое число
с помощью float('nan').

    Реализуйте как обе стратегии, так и solver (алгоритм решения). 
Что касается плюсов и минусов в формуле: возвращайте положительный результат
первым элементов, а отрицательный вторым. Заметьте что solve() должен
возвращать комплексные числа!
"""

import unittest
from abc import ABC
import math
import cmath


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        radical = b ** 2 - 4 * a * c
        return radical


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        radical = b ** 2 - 4 * a * c
        if radical < 0:
            return cmath.nan
        return radical


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        d = self.strategy.calculate_discriminant(a, b, c)
        if d == float('nan') or d is None:
            return float('nan'), float('nan')
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        return x1, x2


class FirstTestSuite(unittest.TestCase):
    def test_ordinary(self):
        a, b, c = "1 10 16".split()
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(int(a), int(b), int(c))
        result = f'{results}'
        self.assertEqual("((-2+0j), (-8+0j))", result)

    def test_real(self):
        a, b, c = "1 10 16".split()
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(int(a), int(b), int(c))
        result = f'{results[0].real} {results[1].imag} '
        result += f'{math.isnan(results[0].real)} {math.isnan(results[1].imag)}'
        self.assertEqual("-2.0 0.0 False False", result)

    def test_real_none(self):
        a, b, c = "1 1 1".split()
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(int(a), int(b), int(c))
        result = f'{math.isnan(results[0])} {math.isnan(results[1])}'
        self.assertEqual("True True", result)


if __name__ == "__main__":
    unittest.main()


