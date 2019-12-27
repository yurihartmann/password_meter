from app.rate.rate import Rate
from app.requirement.requirement import Requirement


class FlatRate(Rate):

    def __init__(self, weight: int):
        super().__init__(weight)

    def calculate(self, requirement: Requirement):
        return requirement.get_count() * self.get_weight()