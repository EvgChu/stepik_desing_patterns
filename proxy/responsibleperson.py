import unittest


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'

class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    def drink(self):
        if self.person.age >= 18:
            return self.person.drink()
        return 'too young'

    def drive(self):
        if self.person.age >= 16:
            return self.person.drive()
        return 'too young'

    def drink_and_drive(self):
        return 'dead'


class Evaluate(unittest.TestCase):
    def test_first(self):
        p = Person(15)
        rp = ResponsiblePerson(p)
        self.assertEqual( "too young",
                         str(rp.drive()))
        self.assertEqual( "too young",
                         str(rp.drink()))
        self.assertEqual( "dead",
                         str(rp.drink_and_drive()))

if __name__ == "__main__":
    unittest.main()
