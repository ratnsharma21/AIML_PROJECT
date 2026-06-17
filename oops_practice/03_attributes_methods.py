class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self.value

calc = Calculator(10)
print(calc.add(5))
