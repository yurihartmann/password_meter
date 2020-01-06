from app.requirement.additions.addition import Addition
from app.password.password import Password
from app.rate.flat_rate import FlatRate


class NumberOfCharacters(Addition):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(4))

    def get_count(self) -> int:
        return len(self.get_password())



