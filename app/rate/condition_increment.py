from app.rate.rate import Rate
from app.requirement.requirement import Requirement


class ConditionIncrement(Rate):

    def __init__(self, weight: int):
        super().__init__(weight)

    def calculate(self, requirement: Requirement):
        length = len(requirement.get_password())
        n = requirement.get_count()
        bonus = (length - n) * self.get_weight()
        return bonus if n > 0 else 0
