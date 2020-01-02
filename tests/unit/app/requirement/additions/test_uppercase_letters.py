import unittest
from unittest.mock import Mock

from app.requirement.additions.uppercase_letters import UppercaseLetters


class TestUppercaseLetters(unittest.TestCase):

    def test_instance(self):
        uppercase_letters = UppercaseLetters(Mock())
        self.assertIsInstance(uppercase_letters, UppercaseLetters)

    def test_method_get_count_with_upper_and_lower_cases_letters_should_be_numbers_of_uppercase_letters(self):
        uppercase_letters = UppercaseLetters(Mock())
        uppercase_letters.password.get_value.return_value = 'AsD123fGh456'
        self.assertEqual(3, uppercase_letters.get_count())

    def test_method_get_bonus_with_upper_and_lower_cases_letters_should_be_bonus(self):
        uppercase_letters = UppercaseLetters(Mock())
        uppercase_letters.password.get_value.return_value = 'AsD123fGh456'
        self.assertEqual(18, uppercase_letters.get_bonus())

    def test_method_get_bonus_with_only_uppercase_letters_should_be_zero(self):
        uppercase_letters = UppercaseLetters(Mock())
        uppercase_letters.password.get_value.return_value = 'ABCDEFGH'
        self.assertEqual(0, uppercase_letters.get_bonus())
