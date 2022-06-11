"""
Требуется реализовать обработчик простых числовых выражений со 
следующими ограничениями:
- в выражениях используются только числовые значения (например, 12), в variables
добавляются переменные, состоящие только из одного символа, из операций 
поддерживаются только сложение и вычитание
- не надо поддерживать скобки или любые другие операции если переменная не 
найдена в variables (или если встречаем переменную, названную более чем одним
символом), то evaluator должен возвращать ноль

в случае любых ошибок с парсингом, evaluator должен возвращать ноль
"""

import unittest
from enum import Enum, auto

class NotValidToken(Exception):
    pass

class Token:
    class Type(Enum):
        VARIABLE = auto()
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text) -> None:
        self.type = type
        self.text = text

    def __str__(self) -> str:
        return f"`{self.text}`"


class Integer:
    def __init__(self, value) -> None:
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self) -> None:
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value
        elif self.left is not None and self.right is None:
            return self.left.value


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        tokens = self._lex(expression)
        try:
            parsed = self._parse(tokens)
        except NotValidToken:
            parsed = Integer(0)
        return parsed.value

    def _lex(self, input):
        result = []
        i = 0
        while i < len(input):
            if input[i] == '+':
                result.append(Token(Token.Type.PLUS, '+'))
            elif input[i] == '-':
                result.append(Token(Token.Type.MINUS, '-'))
            elif input[i] == '(':
                result.append(Token(Token.Type.LPAREN, '('))
            elif input[i] == ')':
                result.append(Token(Token.Type.RPAREN, ')'))
            elif input[i].isalpha():
                variable = [input[i]]
                for j in range(i+1, len(input)):
                    if input[j].isalpha():
                        variable.append(input[j])
                        i += 1
                    else:
                        result.append(Token(Token.Type.VARIABLE,
                                        ''.join(variable)))
                        break
                else:
                    result.append(Token(Token.Type.VARIABLE,
                                        ''.join(variable)))
            else:
                digits = [input[i]]
                for j in range(i+1, len(input)):
                    if input[j].isdigit():
                        digits.append(input[j])
                        i += 1
                    else:
                        result.append(Token(Token.Type.INTEGER,
                                        ''.join(digits)))
                        break
                else:
                    result.append(Token(Token.Type.INTEGER,
                                        ''.join(digits)))
            i += 1

        return result

    def _insert_element(self, root, element):
        if root.left is None:
            root.left = element
        else:
            if root.right is None:
                root.right = element
            else:
                self._insert_element(root.right, element)

    def _insert_operation(self, root, operator):
        if root.type is None:
            root.type = operator
        else:
            if isinstance(root.right, BinaryExpression):
                self._insert_operation(root.right, operator)
            else:
                newroot = BinaryExpression()
                newroot.left = root.right
                newroot.type = operator
                root.right = newroot

    def _invert_operation(self, root):
        if isinstance(root.right, BinaryExpression):
            self._invert_operation(root.right)
        else:
            root.type = BinaryExpression.Type.SUBTRACTION
           

    def _parse(self, tokens):
        result = BinaryExpression()
        was_minus = 1
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.type == Token.Type.INTEGER:
                integer = Integer(was_minus*int(token.text))
                was_minus = 1
                self._insert_element(result, integer)
            elif token.type == Token.Type.VARIABLE:
                if len(token.text) != 1 or token.text not in self.variables:
                    raise NotValidToken
                variable = Integer(was_minus * self.variables[token.text])
                was_minus = 1
                self._insert_element(result, variable)
            elif token.type == Token.Type.PLUS:
                self._insert_operation(result, BinaryExpression.Type.ADDITION)
            elif token.type == Token.Type.MINUS:
                was_minus = -1
                self._insert_operation(result, BinaryExpression.Type.ADDITION)
            elif token.type == Token.Type.LPAREN:
                if was_minus == -1:
                    self._invert_operation(result)
                j = i
                while j < len(tokens):
                    if tokens[j].type == Token.Type.RPAREN:
                        break
                    j += 1
                sub = tokens[i+1:j]
                element = self._parse(sub)
                self._insert_element(result, element)
                i = j
            i += 1
        return result


class FirstTestSuite(unittest.TestCase):
    def test_only_one_number(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("1"), 1)

    def test_only_mumbers(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("1+2+333"), 336)

    def test_only_mumbers_with_curve(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("(1+2)-333"), -330)

    def test_with_define_variable(self):
        ep = ExpressionProcessor()
        ep.variables['x'] = 3
        self.assertEqual(ep.calculate("10-2-x"), 5)

    def test_with_define_variable_and_curve(self):
        ep = ExpressionProcessor()
        ep.variables['x'] = 3
        self.assertEqual(ep.calculate("10-(2-x)"), 11)

    def test_with_bad_variable(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("1+2+xy"), 0)

    def test_with_bad_variable_in_curve(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("1+(2+xy)"), 0)

    def test_with_undefine_variable(self):
        ep = ExpressionProcessor()
        self.assertEqual(ep.calculate("1+2+y"), 0)


if __name__ == "__main__":
    unittest.main()
    