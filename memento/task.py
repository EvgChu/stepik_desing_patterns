"""
    Класс TokenMachine должен хранить токены. Каждый Token это ссылочный объект,
хранящий единственное числовое значение. Машина поддерживание добавление токенов
и, когда токен добавляется, машина возвращает memento (снимок), представляющий
состояние системы на данный момент времени.

    Необходимо заполнить пробел, реализовав паттерн Memento для этого сценария.
Внимательно отнеситесь к сценарию, когда токен передаётся извне как ссылка, а
затем его внутреннее значение извне же и меняется. В таком случае, машина
по-прежнему должна возвращать корректное состояние системы!
"""


import unittest
from copy import deepcopy

class Token:
    def __init__(self, value=0):
        self.value = value

class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return deepcopy(self.tokens)

    def revert(self, memento):
        self.tokens = deepcopy(memento)

class TestMediator(unittest.TestCase):
    def test_main(self):
        tokens_str_vals = "123:R 456".split()

        tm = TokenMachine()
        tokens = []
        mementos = []
        token_index_to_revert = -1
        token_change = None
        for idx, token_str_val in enumerate(tokens_str_vals):
            token_str = token_str_val.split(':')

            val = None
            if len(token_str) == 1:
                # print(token_str[0])
                val = int(token_str[0])
            else:
                # print(token_str[0])
                val = int(token_str[0])
                if token_str[1] == 'R':
                    token_index_to_revert = idx
                elif token_str[1][0] == 'C':
                    token_change = (val, int(token_str[1][1]))

            t = Token(val)
            m = tm.add_token_value(t.value)

            tokens.append(t)
            mementos.append(m)

        if token_change:
            tokens[token_change[1]].value = token_change[0]

        tm.revert(mementos[token_index_to_revert])

        result = f'{len(tm.tokens)} '

        for t in tm.tokens:
            result += str(t.value)

        self.assertEqual(result, "1 123")



if __name__ == "__main__":
    unittest.main()


