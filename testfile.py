from main import Calc
import main
import unittest

class MyTestCase(unittest.TestCase):

    def SetUp(self):

        self.example = Calc()
        self.call_calculating = self.example.calculating()

    def test_string_input(self):
        self.get_expression = main.expression
        if type(self.get_expression) != str:
            assert AssertionError

    def test_valid_string_input(self):
        self.testdata = '1*10-50000+200'
        main.expression = self.testdata
        self.res = self.call_calculating()
        self.assertEqual(self.res, '-49790')
        pass


if __name__ == '__main__':
    unittest.main()

