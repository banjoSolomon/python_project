from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, nin, sales, rate):
        self._first_name = first_name
        self._last_name = last_name
        self._nin = nin
        self._sales = sales
        self._rate = rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def nin(self):
        return self._nin

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError(f"Invalid amount{value}")
        self._sales = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rates):
        if rates < Decimal(0.0) < rates < Decimal(1.0):
            raise ValueError("Invalid rate amount")
        self._rate = rates

    def earning(self):
        return self.sales * (self.rate / 100)

    def __repr__(self):
        return f"First Name: {self.first_name}\nLast Name: {self._last_name}\n" \
               f"Nin: {self._nin}\n Earning: {self.earning()}"


Solomon = CommissionEmployee("Ayomide", "Banjo", 23458689, 5000, 5.0)

print(Solomon)
