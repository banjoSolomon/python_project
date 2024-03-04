from collections import namedtuple
from dataclasses import dataclass
from decimal import Decimal

Player = namedtuple(typename="Player", field_names=["name"])

p1 = Player("solomon")
print(p1)


@dataclass(order=True)
class Account:
    name: str
    balance = Decimal

    def withdraw(self, amount: Decimal):
        return self.balance - amount
