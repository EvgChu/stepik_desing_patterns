import unittest

class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        password = [str(i) for i in combination]
        self.password = "".join(password)

    def reset(self):
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        if self.status == "LOCKED":
            self.status = str(digit)
        else:
            self.status += str(digit)

        if not self.password.startswith(self.status):
            self.status = "ERROR"
            return

        if self.status == self.password:
            self.status = "OPEN"

class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

    def test_failed(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(5)
        self.assertEqual('ERROR', cl.status)

    def test_reset(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.reset()
        self.assertEqual('LOCKED', cl.status)

if __name__ == "__main__":
    unittest.main()