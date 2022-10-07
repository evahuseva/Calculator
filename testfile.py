from main import Calc
import main
import unittest
import logging


class MyTestCase(unittest.TestCase):

    #    def SetUp(self):
    #        example = Calc()
    #        self.call_calculating = example.calculating()

    def test_string_input(self):
        self.get_expression = main.expression
        if type(self.get_expression) != str:
            raise TypeError

    def test_valid_string_input(self):
        main.expression = '1*10-50000+200'
        example = Calc()
        self.call_calculating = str(example.calculating())
        try:
            self.assertEqual(self.call_calculating, '-49790')
        except Exception as e:
            raise e


if __name__ == '__main__':
    unittest.main()
