class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return complex(self.left + other.left and self.right + other.right)

    def __sub__(self, other):
        return complex(self.left - other.left and self.right - other.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left > other.left and self.right > other.right

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.left
        return complex(self.left, self.right)

    def __isub__(self, other):
        self.left -= other.left
        self.right -= other.left
        return complex(self.left, self.right)


c1 = complex(2, 3)
c2 = complex(5, -2)
c3 = complex(2, 3)
print(c1)
print(c2)
print(c1 - c2)
print(c1 == c2)
print(c1 != c3)
c1 += c2
c1 -= c2
print(c1)
print(c1)
