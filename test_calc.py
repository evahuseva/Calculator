from main import Calc
import main
import unittest
import re
import logging


class MyTestCase(unittest.TestCase):

    #    def SetUp(self):
    #        example = Calc()
    #        self.call_calculating = example.calculating()

    def test_string_input(self):
        self.get_expression = main.expression
        if type(self.get_expression) != str:
            raise TypeError

    def test_valid_input(self):
        self.get_expression = main.expression
        self.isvalid = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', main.expression) is None
        try:
            if self.isvalid:
                return main.expression
        except SyntaxError:
            assert SyntaxError

    def test_calculation(self):
        main.expression = '1*10-50000+200'
        example = Calc()

        self.call_calculating = str(example.calculating())
        if self.assertEqual(self.call_calculating, '-49790'):
            pass
        else:
            assert 'problem'


if __name__ == '__main__':
    unittest.main()
