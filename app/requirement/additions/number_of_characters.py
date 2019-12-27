from app.requirement.additions.additions import Additions
from app.password.password import Password
from app.rate.flat_rate import FlatRate


class NumberOfCharacters(Additions):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(4))

    def get_count(self) -> int:
        return len(self.password.get_value())



