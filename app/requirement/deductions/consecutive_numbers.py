from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.deductions.deduction import Deduction


class ConsecutiveNumbers(Deduction):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(2))

    def get_count(self) -> int:
        cont = 0
        last_char = ''

        for char in self.get_password():
            if char.isnumeric() and last_char.isnumeric():
                cont += 1
            last_char = char

        return cont
