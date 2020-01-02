from app.password.password import Password
from app.rate.flat_rate import FlatRate
from app.requirement.additions.addition import Addition
from app.requirement.additions.symbols import Symbols


class MinimumRequirements(Addition):

    def __init__(self, password: Password):
        super().__init__(password, FlatRate(2))

    def get_count(self) -> int:
        sum_minimum_requirements = 0

        items_minimum_requirements = [
            self.has_lowercase_letters(),
            self.has_uppercase_letters(),
            self.has_numbers(),
            self.has_symbols(),
            self.has_minimum_8_characters()
        ]

        for item in items_minimum_requirements:
            if item:
                sum_minimum_requirements += 1

        return sum_minimum_requirements

    def has_lowercase_letters(self) -> bool:
        lowercase_letters = [char for char in self.password.get_value() if char.islower()]
        return True if len(lowercase_letters) > 0 else False

    def has_uppercase_letters(self) -> bool:
        uppercase_letters = [char for char in self.password.get_value() if char.isupper()]
        return True if len(uppercase_letters) > 0 else False

    def has_numbers(self) -> bool:
        numbers = [char for char in self.password.get_value() if char.isnumeric()]
        return True if len(numbers) > 0 else False

    def has_symbols(self) -> bool:
        symbols = [char for char in self.password.get_value() if Symbols.is_symbol(char)]
        return True if len(symbols) > 0 else False

    def has_minimum_8_characters(self) -> bool:
        return True if len(self.password.get_value()) >= 8 else False
