import unittest
from unittest.mock import Mock

from app.requirement.deductions.consecutive_numbers import ConsecutiveNumbers


class TestConsecutiveNumbers(unittest.TestCase):

    def test_instance(self):
        consecutive_uppercase_letters = ConsecutiveNumbers(Mock())
        self.assertIsInstance(consecutive_uppercase_letters, ConsecutiveNumbers)

    def test_method_get_count_with_consecutive_uppercase_letters_should_be_count_of_letters(self):
        consecutive_uppercase_letters = ConsecutiveNumbers(Mock())
        consecutive_uppercase_letters.password.get_value.return_value = 'aAAAdd1rR2Rr333G441gg'
        self.assertEqual(4, consecutive_uppercase_letters.get_count())

    def test_method_get_count_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_uppercase_letters = ConsecutiveNumbers(Mock())
        consecutive_uppercase_letters.password.get_value.return_value = 'aAAAdd1rR2Rr3G4gg'
        self.assertEqual(0, consecutive_uppercase_letters.get_count())

    def test_method_get_bonus_with_consecutive_uppercase_letters_should_bonus(self):
        consecutive_uppercase_letters = ConsecutiveNumbers(Mock())
        consecutive_uppercase_letters.password.get_value.return_value = 'aAAAdd1rR2Rr33G41gg'
        self.assertEqual(-4, consecutive_uppercase_letters.get_bonus())

    def test_method_get_bonus_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_uppercase_letters = ConsecutiveNumbers(Mock())
        consecutive_uppercase_letters.password.get_value.return_value = 'aAAAdd1rR2Rr3G4gg'
        self.assertEqual(0, consecutive_uppercase_letters.get_bonus())
