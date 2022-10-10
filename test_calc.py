from main import Calc

class CalculatorTests():

    def test_calculation1(self):
        test1 = Calc('1*10-50000+200').output()
        self.assertEqual(test1, -49790)
