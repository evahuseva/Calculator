import re


class Calc:

    def __init__(self):
        self.isvalid = None
        self.result = None

    def validate_input(self):
        self.isvalid = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', expression) is None
        if self.isvalid:
            return expression
        else:
            assert expression, 'Invalid syntax'

    def calculating(self):
        self.result = eval(str(self.validate_input()))
        return self.result


expression = input("Enter the expression: ")

c1 = Calc()
print(c1.calculating())
