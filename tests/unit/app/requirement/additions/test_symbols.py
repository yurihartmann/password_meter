import unittest
from unittest.mock import Mock

from app.requirement.additions.symbols import Symbols


class TestSymbols(unittest.TestCase):

    def test_instance(self):
        symbols = Symbols(Mock())
        self.assertIsInstance(symbols, Symbols)

    def test_get_count_should_be_numbers_of_symbols(self):
        symbols = Symbols(Mock())
        symbols._password.get_value.return_value = 'isbhduqwbquibduiw!@$*-+...,,,'
        self.assertEqual(12, symbols.get_count())

    def test_get_bonus_should_be_bonus(self):
        symbols = Symbols(Mock())
        symbols._password.get_value.return_value = 'isbhduqwbquibduiw!@$*-+...,,,'
        self.assertEqual(72, symbols.get_bonus())
