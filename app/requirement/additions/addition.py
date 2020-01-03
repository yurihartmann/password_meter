from abc import ABC, abstractmethod

from app.requirement.requirement import Requirement
from app.password.password import Password
from app.rate.rate import Rate


class Addition(Requirement, ABC):

    def __init__(self, password: Password, rate: Rate):
        super().__init__(password, rate)
