class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print("f{self.name} sleeping...")

    def eat(self):
        print("eating...")

    def __str__(self):
        return f"{self.name} {self.gender}"


h1 = Human(4.1, "male", 'bolaji')
h2 = Human(3.5, "female", 'hannah')
print(h1.number_of_eyes)
print(h2.number_of_eyes)
name = 'dayo'
print(type(name))
print(h1.sleep())
print(h2.sleep())
print(h1)
