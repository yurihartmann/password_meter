from abc import ABC

from app.requirement.requirement import Requirement
from app.password.password import Password
from app.rate.rate import Rate


class Deduction(Requirement, ABC):

    def __init__(self, password: Password, rate: Rate):
        super().__init__(password, rate)

    def get_bonus(self) -> int:
        return self._rate.calculate(self) * -1

