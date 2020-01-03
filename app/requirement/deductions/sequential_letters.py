from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.deductions.deduction import Deduction


class SequentialLetters(Deduction):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(3))

    def get_count(self) -> int:
        return self.get_sequential_letters() + self.get_sequential_reversed_letters()

    def get_sequential_letters(self) -> int:
        total = 0
        cont = 0
        last_letter = self._password.get_value()[0]

        for char in self._password.get_value():
            if not char.isalpha():
                last_letter = char
                continue

            if ord(last_letter) + 1 == ord(char.lower()):
                cont += 1 if cont > 0 else 2
            else:
                total += cont - 2 if cont >= 3 else 0
                cont = 0

            last_letter = char.lower()

        total += cont - 2 if cont >= 3 else 0
        return total

    def get_sequential_reversed_letters(self) -> int:
        total = 0
        cont = 0
        last_letter = self._password.get_value()[0]

        for char in self._password.get_value():
            if not char.isalpha():
                last_letter = char
                continue

            if ord(last_letter) - 1 == ord(char.lower()):
                cont += 1 if cont > 0 else 2
            else:
                total += cont - 2 if cont >= 3 else 0
                cont = 0

            last_letter = char.lower()

        total += cont - 2 if cont >= 3 else 0
        return total

