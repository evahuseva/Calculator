from calculator import *
import pytest


def test_calculation1():
    test1 = Calc('1*10-50000+200').output()
    assert test1, -49790


if __name__ == '__calculator__':
    pytest.calculator()
