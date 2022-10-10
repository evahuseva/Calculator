import main
from main import Calc
import unittest
from unittest import mock
from unittest.mock import patch
from unittest import TestCase


class CalculatorTests(unittest.TestCase):

    @patch('main.input', return_value='1*10-50000+200')
    def test_multiplication(self, mock_input):
        res = Calc.output()
        self.assertEqual(res, '-49790')


if __name__ == '__main__':
    unittest.main()
