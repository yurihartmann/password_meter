from itertools import count

from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.deductions.deduction import Deduction


class SequentialNumbers(Deduction):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(3))

    def get_count(self) -> int:
        return self.get_sequential_numbers() + self.get_sequential_reversed_numbers()

    def get_sequential_numbers(self) -> int:
        total = 0
        cont = 0
        last_number = self._password.get_value()[0]

        for char in self._password.get_value():
            if not char.isnumeric():
                last_number = None
                continue
            else:
                number = int(char)

            if last_number and int(last_number) + 1 == number:
                cont += 1 if cont > 0 else 2
            else:
                total += cont - 2 if cont >= 3 else 0
                cont = 0

            last_number = number

        total += cont - 2 if cont >= 3 else 0
        return total

    def get_sequential_reversed_numbers(self) -> int:
        total = 0
        cont = 0
        last_number = self._password.get_value()[0]

        for char in self._password.get_value():
            if not char.isnumeric():
                last_number = None
                continue
            else:
                number = int(char)

            if last_number and int(last_number) - 1 == number:
                cont += 1 if cont > 0 else 2
            else:
                total += cont - 2 if cont >= 3 else 0
                cont = 0

            last_number = number

        total += cont - 2 if cont >= 3 else 0
        return total
