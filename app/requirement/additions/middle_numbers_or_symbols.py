from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.additions.addition import Addition
from app.requirement.additions.symbols import Symbols


class MiddleNumbersOrSymbols(Addition):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(2))

    def get_count(self) -> int:
        cuted_password = self.get_password().strip()[1:-1]
        cont = 0
        for char in cuted_password:
            if Symbols.is_symbol(char) or char.isnumeric():
                cont += 1
        return cont
