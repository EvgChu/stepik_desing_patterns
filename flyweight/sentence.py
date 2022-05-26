import unittest

class Sentence:
    def __init__(self, plain_text) -> None:
        self.plain_text = plain_text.split(' ')
        self.formatting = []
    class TextRange:
        def __init__(self, position, capitalize=False):
            self._position = position
            self.capitalize = capitalize
            
        def covers(self, position):
            return self._position == position

    def __getitem__(self, index):
        range = self.TextRange(index)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            word = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    word = word.upper()
            result.append(word)
        return ' '.join(result)

class Evaluate(unittest.TestCase):
    def test_first(self):
        sentence = Sentence('hello world')
        sentence[1].capitalize = True 
        self.assertEqual( "hello WORLD",
                         str(sentence))

if __name__ == "__main__":
    unittest.main()
