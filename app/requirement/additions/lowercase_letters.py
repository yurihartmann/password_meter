from app.requirement.additions.addition import Addition
from app.password.password import Password
from app.rate.condition_increment import ConditionIncrement


class LowercaseLetters(Addition):

    def __init__(self, password: Password):
        super().__init__(password, ConditionIncrement(2))

    def get_count(self) -> int:
        letters_lower_case = [letter for letter in self.get_password() if letter.islower()]
        return len(letters_lower_case)
