import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.additions.symbols import Symbols


class TestSymbols(unittest.TestCase):

    def setUp(self) -> None:
        self.password_mock = Mock()
        self.password_mock.get_value = MagicMock(return_value=' $5%%( %%@#*(@#')
        self.symbols = Symbols(self.password_mock)

    def test_instance(self):
        self.assertIsInstance(self.symbols, Symbols)

    def test_get_count_should_be_numbers_of_symbols(self):
        self.assertEqual(12, self.symbols.get_count())

