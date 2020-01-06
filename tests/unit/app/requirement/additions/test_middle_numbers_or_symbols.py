import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.additions.middle_numbers_or_symbols import MiddleNumbersOrSymbols


class TestMiddleNumbersOrSymbols(unittest.TestCase):

    def test_instance(self):
        middle_numbers_or_symbols = MiddleNumbersOrSymbols(Mock())
        self.assertIsInstance(middle_numbers_or_symbols, MiddleNumbersOrSymbols)

    def test_get_count_method_should_be_numbers_of_middle_nubers_and_symbols(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='.11111a213213213213asdfasdf2,1a  !!  ')
        middle_numbers_or_symbols = MiddleNumbersOrSymbols(password_mock)
        self.assertEqual(21, middle_numbers_or_symbols.get_count())

    def test_get_bonus_method_be_return_bonus(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='.11111a213213213213asdfasdf2,1a')
        middle_numbers_or_symbols = MiddleNumbersOrSymbols(password_mock)
        self.assertEqual(40, middle_numbers_or_symbols.get_bonus())

