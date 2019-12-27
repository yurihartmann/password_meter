from app.requirement.additions.additions import Additions
from app.password.password import Password
from app.rate.condition_increment import ConditionIncrement


class UppercaseLetters(Additions):

    def __init__(self, password: Password):
        super().__init__(password, ConditionIncrement(2))

    def get_count(self) -> int:
        return len([letter for letter in self.password.get_value() if letter.isupper()])
