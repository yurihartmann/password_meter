import unittest
from unittest.mock import Mock

from app.requirement.deductions.consecutive_lowercase_letters import ConsecutiveLowercaseLetters


class TestConsecutiveLowercaseLetters(unittest.TestCase):

    def test_instance(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        self.assertIsInstance(consecutive_lowercase_letters, ConsecutiveLowercaseLetters)

    def test_method_get_count_with_consecutive_uppercase_letters_should_be_count_of_letters(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        consecutive_lowercase_letters._password.get_value.return_value = 'aAAAddrRRrGgg'
        self.assertEqual(3, consecutive_lowercase_letters.get_count())

    def test_method_get_count_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        consecutive_lowercase_letters._password.get_value.return_value = 'aAdRrGg24Df'
        self.assertEqual(0, consecutive_lowercase_letters.get_count())

    def test_method_get_bonus_with_consecutive_uppercase_letters_should_bonus(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        consecutive_lowercase_letters._password.get_value.return_value = 'aaaarrRft123HHrtyu'
        self.assertEqual(-18, consecutive_lowercase_letters.get_bonus())

    def test_method_get_bonus_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        consecutive_lowercase_letters._password.get_value.return_value = 'aAdRrGg24Df'
        self.assertEqual(0, consecutive_lowercase_letters.get_bonus())
