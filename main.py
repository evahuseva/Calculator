import re

def calculator():
    pattern = "[a-zA-Z]+"
    expression = input("Enter the expression: ")
    if re.search(pattern, expression):
        return "Invalid input! No characters allowed."
    else:
        return eval(expression)


print(calculator())

# r1 = re.findall(r"^\w+",expression)
# print(r1)