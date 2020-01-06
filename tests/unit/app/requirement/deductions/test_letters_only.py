import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.deductions.letters_only import LettersOnly


class TestLettersOnly(unittest.TestCase):

    def test_instance(self):
        letters_only = LettersOnly(Mock())
        self.assertIsInstance(letters_only, LettersOnly)

    def test_method_get_count_with_only_letters_should_be_count_of_letters(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aaAaaAaa')
        letters_only = LettersOnly(password_mock)
        self.assertEqual(8, letters_only.get_count())

    def test_method_get_count_with_not_only_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='a1a2a3a4')
        letters_only = LettersOnly(password_mock)
        self.assertEqual(0, letters_only.get_count())

    def test_method_get_bonus_with_only_letters_should_be_count_of_letters(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aaAaaAaa')
        letters_only = LettersOnly(password_mock)
        self.assertEqual(-8, letters_only.get_bonus())

    def test_method_get_bonus_with_not_only_letters_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='a1a2a3a4')
        letters_only = LettersOnly(password_mock)
        self.assertEqual(0, letters_only.get_bonus())

