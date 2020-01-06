import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.additions.uppercase_letters import UppercaseLetters


class TestUppercaseLetters(unittest.TestCase):

    def setUp(self) -> None:
        self.password_mock = Mock()
        self.password_mock.get_value = MagicMock(return_value='AsD123fGh456')
        self.uppercase_letters = UppercaseLetters(self.password_mock)

    def test_instance(self):
        self.assertIsInstance(self.uppercase_letters, UppercaseLetters)

    def test_method_get_count_with_upper_and_lower_cases_letters_should_be_numbers_of_uppercase_letters(self):
        self.assertEqual(3, self.uppercase_letters.get_count())

    def test_method_get_bonus_with_upper_and_lower_cases_letters_should_be_bonus(self):
        self.assertEqual(18, self.uppercase_letters.get_bonus())

    def test_method_get_bonus_with_only_uppercase_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='ABCDEFGH')
        uppercase_letters = UppercaseLetters(password_mock)
        self.assertEqual(0, uppercase_letters.get_bonus())
