from abc import ABC, abstractmethod

from app.password.password import Password
from app.rate.rate import Rate


class Requirement(ABC):

    def __init__(self, password: Password, rate: Rate):
        self._password = password
        self._rate = rate

    def get_bonus(self):
        return self._rate.calculate(self)

    @abstractmethod
    def get_count(self):
        pass

    def get_password(self) -> str:
        return self._password.get_value()

