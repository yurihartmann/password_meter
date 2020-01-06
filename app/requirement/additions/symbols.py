from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.additions.addition import Addition


class Symbols(Addition):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(6))

    def get_count(self) -> int:
        cont = 0
        for char in self.get_password():
            if self.is_symbol(char):
                cont += 1
        return cont

    @classmethod
    def is_symbol(self, char: str) -> bool:
        if not char.isnumeric() and not char.isalpha() and char != ' ':
            return True
        else:
            return False
