import re


class Calc:

    def __init__(self):
        self.isvalid = None
        self.result = None

    def calculating(self):
#        try:
            self.result = eval(str(expression))
            return self.result
#        except SyntaxError:
#            print('Invalid expression input.')


expression = input("Enter the expression: ")

c1 = Calc()
print(c1.calculating())
