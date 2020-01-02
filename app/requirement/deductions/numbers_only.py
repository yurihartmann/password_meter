from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.deductions.deduction import Deduction


class NumbersOnly(Deduction):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(1))

    def get_count(self) -> int:
        cont = 0
        for char in self.password.get_value():
            if not char.isnumeric():
                return 0
            cont += 1
        return cont
