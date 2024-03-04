class Define:
    def __init__(self):
        self.check = ""

    def getString(self, check):
        self.check = check

    def printString(self):
        return self.check.upper()


digits = list(range(1, 51))

# def check_even(number):
#   return number % 2 == 0
ans = list(filter(lambda number: number % 2 == 0, digits))
print(ans)
