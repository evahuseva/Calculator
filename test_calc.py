import main
from main import Calc
import unittest


class CalculatorTests(unittest.TestCase):

#    @patch('main.input', lambda *args: '1*10-50000+200')
    def test_calculation1(self):
        test1 = Calc('1*10-50000+200').output()
#        Mock('1*10-50000+200')
        self.assertEqual(test1, -49790)
#
#    def test_calculation2(self):
#        test2 = Calc('1-1-1').output()
#        self.assertEqual(test2, -49790)


if __name__ == '__main__':
    unittest.main()
