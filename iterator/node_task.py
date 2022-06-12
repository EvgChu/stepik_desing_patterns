"""
    Вам дано определение класса Node. Пожалуйста, реализуйте preorder 
traversal прямо в классе Node.
    Возвращаемая последовательность должна быть последовательностью значений,
а не самих узлов.
"""

import unittest

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current):
            yield current
            if current.left:
                for left in traverse(current.left):
                    yield left
            if current.right:
                for right in traverse(current.right):
                    yield right
        for node in traverse(self):
            yield node.value


    def traverse_postorder(self):
        def traverse(current):
            if current.left:
                for left in traverse(current.left):
                    yield left
            if current.right:
                for right in traverse(current.right):
                    yield right
            yield current

        for node in traverse(self):
            yield node.value

    def traverse_in_order(self):
        def traverse(current):
            if current.left:
                for left in traverse(current.left):
                    yield left
            yield current
            if current.right:
                for right in traverse(current.right):
                    yield right
        for node in traverse(self):
            yield node


class TestNode(unittest.TestCase):
    def test_traverse_preorder(self):
        a, b, c, d, e = [i for i in "abcde"]
        node = Node(a,
                        Node(b,
                            Node(c),
                            Node(d)),
                        Node(e))

        self.assertEqual('abcde',''.join([x for x in node.traverse_preorder()]))

    def test_traverse_postorder(self):
        a, b, c, d, e = [i for i in "abcde"]
        node = Node(e,
                        Node(c,
                            Node(a),
                            Node(b)),
                        Node(d))

        self.assertEqual('abcde',''.join([x for x in node.traverse_postorder()]))


if __name__ == "__main__":
    unittest.main()

