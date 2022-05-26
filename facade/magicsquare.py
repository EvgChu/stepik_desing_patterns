 
from random import randint 
import unittest


class Generator:
    def generate(self, count):
        return [randint(1,9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self):
        self.result = []

    def generate(self, size):
        return self.result

    def __str__(self):
        for row in self.result:
            for col in row:
                print(col, sep="\t")
            print()


class MagicSquareGeneratorRandom(MagicSquareGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        # todo - return a magic square of the given size
        is_magic_square = False

        while not is_magic_square:
            square = self._generate_random_square(size)
            is_magic_square = self._is_magic_square(square)
        
        return square

    def _is_magic_square(self, square):
        square_sections = self.splitter.split(square)
        return self.verifier.verify(square_sections)

    def _generate_random_square(self, size):
        return [self.generator.generate(size) for _ in range(size)]


class MagicSquareGeneratorSimple(MagicSquareGenerator):
    def generate(self, size):
        result = []
        gen = Generator()
        seq = gen.generate(size)
        for row in range(size):
            result.append(seq[row:]+seq[:row])
        return result


class Evaluate(unittest.TestCase):
    def test_first(self):
        gen = MagicSquareGeneratorRandom()
        parameter = randint(2,4)
        square = gen.generate(int(parameter))
        v = Verifier()
        self.assertEqual( True,
                         v.verify(square))
        self.assertEqual( parameter,
                         len(square))
        self.assertEqual( parameter,
                         len(square[0]))

    def test_second(self):
        gen = MagicSquareGeneratorSimple()
        parameter = randint(5,9)
        square = gen.generate(int(parameter))
        v = Verifier()
        self.assertEqual( True,
                         v.verify(square))
        self.assertEqual( parameter,
                         len(square))
        self.assertEqual( parameter,
                         len(square[0]))




if __name__ == "__main__":
    unittest.main()