import main
from main import Calc
import unittest


class CalculatorTests(unittest.TestCase):

    def test_calculation1(self):
        test1 = Calc('1*10-50000+200').output()
        self.assertEqual(test1, -49790)


if __name__ == '__main__':
    unittest.main()
