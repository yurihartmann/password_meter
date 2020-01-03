import unittest
from unittest.mock import Mock

from app.requirement.deductions.consecutive_uppercase_letters import ConsecutiveUppercaseLetters


class TestConsecutiveUppercaseLetters(unittest.TestCase):

    def test_instance(self):
        consecutive_uppercase_letters = ConsecutiveUppercaseLetters(Mock())
        self.assertIsInstance(consecutive_uppercase_letters, ConsecutiveUppercaseLetters)

    def test_method_get_count_with_consecutive_uppercase_letters_should_be_count_of_letters(self):
        consecutive_uppercase_letters = ConsecutiveUppercaseLetters(Mock())
        consecutive_uppercase_letters._password.get_value.return_value = 'aAAAEEEEEddrgRRrGgg'
        self.assertEqual(8, consecutive_uppercase_letters.get_count())

    def test_method_get_count_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_uppercase_letters = ConsecutiveUppercaseLetters(Mock())
        consecutive_uppercase_letters._password.get_value.return_value = 'aAdrRrGg24hnd'
        self.assertEqual(0, consecutive_uppercase_letters.get_count())

    def test_method_get_bonus_with_consecutive_uppercase_letters_should_bonus(self):
        consecutive_uppercase_letters = ConsecutiveUppercaseLetters(Mock())
        consecutive_uppercase_letters._password.get_value.return_value = 'aAAAddrRRrGgg'
        self.assertEqual(-6, consecutive_uppercase_letters.get_bonus())

    def test_method_get_bonus_without_consecutive_uppercase_letters_should_be_zero(self):
        consecutive_uppercase_letters = ConsecutiveUppercaseLetters(Mock())
        consecutive_uppercase_letters._password.get_value.return_value = 'aAdrRrGg24hnd'
        self.assertEqual(0, consecutive_uppercase_letters.get_bonus())
