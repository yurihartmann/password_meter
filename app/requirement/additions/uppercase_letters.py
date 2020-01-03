from app.requirement.additions.addition import Addition
from app.password.password import Password
from app.rate.condition_increment import ConditionIncrement


class UppercaseLetters(Addition):

    def __init__(self, password: Password):
        super().__init__(password, ConditionIncrement(2))

    def get_count(self) -> int:
        return len([letter for letter in self._password.get_value() if letter.isupper()])
