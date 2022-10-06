from main import Calc
import main
import unittest
import operator
import re

example1 = Calc()
function1 = example1.calculating()


class MyTestCase(unittest.TestCase):

    def test_valid_input(self):
        self.data = '1*10-50000+200'
#        self.valids = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', self.data) is None
        self.result = function1(self.data)
        self.assertEqual(self.result, -49790)

    def test_valid_input_error(self):
        self.data = '1*10-50000abc'
        self.result = function1(self.data)
#       self.valids = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', self.data) is None
        self.assertRaises(SyntaxError)
        assert 'Invalid input'

    def test_add(self):
        self.data = '1+2+3'
        self.result = function1(self.data)
        self.assertEqual(self.result, 6)

    def test_add_error(self):
        self.data = '1+2+3'
        self.result = function1
        self.assertEqual(self.result, 0)

    def test_subtract(self):
        self.data = '1-2-3'
        self.result = function1
        self.assertEqual(self.result, -5)

    def test_subtract_error(self):
        self.data = '1-2-3'
        self.result = function1
        self.assertEqual(self.result, 0)

    def test_multipy(self):
        self.data = '1*2*3*4*5*6*7-8*9*10*11'
        self.result = function1
        self.assertEqual(self.result, -2880)

    def test_multipy_error(self):
        self.data = '1*2*3*4*5*6*7-8*9*10*11'
        self.result = function1
        self.assertEqual(self.result, 0)


if __name__ == '__main__':
    unittest.main()
