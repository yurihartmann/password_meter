from app.requirement.additions.addition import Addition
from app.password.password import Password
from app.rate.condition import Condition


class Numbers(Addition):

    def __init__(self, password: Password):
        super().__init__(password, Condition(4))

    def get_count(self) -> int:
        numbers = [char for char in self.password.get_value() if char.isnumeric()]
        return len(numbers)


