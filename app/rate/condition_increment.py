from app.rate.rate import Rate
from app.requirement.requirement import Requirement


class ConditionIncrement(Rate):

    def __init__(self, weight: int):
        super().__init__(weight)

    def calculate(self, requirement: Requirement):
        length = len(requirement.password.get_value())
        n = requirement.get_count()
        return (length - n) * self.get_weight()