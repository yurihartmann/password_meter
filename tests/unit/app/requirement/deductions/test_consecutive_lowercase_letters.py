import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.deductions.consecutive_lowercase_letters import ConsecutiveLowercaseLetters


class TestConsecutiveLowercaseLetters(unittest.TestCase):

    def test_instance(self):
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(Mock())
        self.assertIsInstance(consecutive_lowercase_letters, ConsecutiveLowercaseLetters)

    def test_method_get_count_with_consecutive_uppercase_letters_should_be_count_of_letters(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aAAAddrRRrGgg')
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(password_mock)
        self.assertEqual(3, consecutive_lowercase_letters.get_count())

    def test_method_get_count_without_consecutive_uppercase_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aAdRrGg24Df')
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(password_mock)
        self.assertEqual(0, consecutive_lowercase_letters.get_count())

    def test_method_get_bonus_with_consecutive_uppercase_letters_should_bonus(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aaaarrRft123HHrtyu')
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(password_mock)
        self.assertEqual(-18, consecutive_lowercase_letters.get_bonus())

    def test_method_get_bonus_without_consecutive_uppercase_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aAdRrGg24Df')
        consecutive_lowercase_letters = ConsecutiveLowercaseLetters(password_mock)
        self.assertEqual(0, consecutive_lowercase_letters.get_bonus())
