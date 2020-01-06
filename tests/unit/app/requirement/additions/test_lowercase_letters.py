import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.additions.lowercase_letters import LowercaseLetters


class TestLowercaseLetters(unittest.TestCase):

    def test_instance(self):
        lowercase_letters = LowercaseLetters(Mock())
        self.assertIsInstance(lowercase_letters, LowercaseLetters)

    def test_method_get_count_with_upper_and_lower_cases_letters_should_be_numbers_of_lowercase_letters(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='asD123fGh456')
        lowercase_letters = LowercaseLetters(password_mock)
        self.assertEqual(4, lowercase_letters.get_count())

    def test_method_get_bonus_with_upper_and_lower_cases_letters_should_be_bonus(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='AsD123fGh456')
        lowercase_letters = LowercaseLetters(password_mock)
        self.assertEqual(18, lowercase_letters.get_bonus())

    def test_method_get_bonus_with_lower_and_without_lower_cases_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='abcdefgh')
        lowercase_letters = LowercaseLetters(password_mock)
        self.assertEqual(0, lowercase_letters.get_bonus())
