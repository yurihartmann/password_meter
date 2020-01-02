from abc import ABC, abstractmethod

from app.password.password import Password
from app.rate.rate import Rate

class Requirement(ABC):

    def __init__(self, password: Password, rate: Rate):
        self.password = password
        self.rate = rate

    def get_bonus(self):
        return self.rate.calculate(self)

    @abstractmethod
    def get_count(self):
        raise NotImplemented('NotImplemented get_count')