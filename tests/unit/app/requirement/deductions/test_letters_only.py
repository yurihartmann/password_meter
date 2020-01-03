import unittest
from unittest.mock import Mock

from app.requirement.deductions.letters_only import LettersOnly


class TestLettersOnly(unittest.TestCase):

    def test_instance(self):
        letters_only = LettersOnly(Mock())
        self.assertIsInstance(letters_only, LettersOnly)

    def test_method_get_count_with_only_letters_should_be_count_of_letters(self):
        letters_only = LettersOnly(Mock())
        letters_only._password.get_value.return_value = 'aaAaaAaa'
        self.assertEqual(8, letters_only.get_count())

    def test_method_get_count_with_not_only_letters_should_be_zero(self):
        letters_only = LettersOnly(Mock())
        letters_only._password.get_value.return_value = 'a1a2a3a4'
        self.assertEqual(0, letters_only.get_count())

    def test_method_get_bonus_with_only_letters_should_be_count_of_letters(self):
        letters_only = LettersOnly(Mock())
        letters_only._password.get_value.return_value = 'aaAaaAaa'
        self.assertEqual(-8, letters_only.get_bonus())

    def test_method_get_bonus_with_not_only_letters_should_be_zero(self):
        letters_only = LettersOnly(Mock())
        letters_only._password.get_value.return_value = 'a1a2a3a4'
        self.assertEqual(0, letters_only.get_bonus())

