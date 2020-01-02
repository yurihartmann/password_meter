import unittest
from unittest.mock import Mock

from app.requirement.additions.lowercase_letters import LowercaseLetters


class TestLowercaseLetters(unittest.TestCase):

    def test_instance(self):
        lowercase_letters = LowercaseLetters(Mock())
        self.assertIsInstance(lowercase_letters, LowercaseLetters)

    def test_method_get_count_with_upper_and_lower_cases_letters_should_be_numbers_of_lowercase_letters(self):
        lowercase_letters = LowercaseLetters(Mock())
        lowercase_letters.password.get_value.return_value = 'asD123fGh456'
        self.assertEqual(4, lowercase_letters.get_count())

    def test_method_get_bonus_with_upper_and_lower_cases_letters_should_be_bonus(self):
        lowercase_letters = LowercaseLetters(Mock())
        lowercase_letters.password.get_value.return_value = 'AsD123fGh456'
        self.assertEqual(18, lowercase_letters.get_bonus())

    def test_method_get_bonus_with_lower_and_without_lower_cases_letters_should_be_zero(self):
        lowercase_letters = LowercaseLetters(Mock())
        lowercase_letters.password.get_value.return_value = 'abcdefgh'
        self.assertEqual(0, lowercase_letters.get_bonus())
