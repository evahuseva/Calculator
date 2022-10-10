from calculator import Calc


def test_calculation1():
    test_value = Calc('1*10-50000+200').output()
    assert -49790 == test_value
