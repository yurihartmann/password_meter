import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.deductions.numbers_only import NumbersOnly


class TestNumbersOnly(unittest.TestCase):

    def test_instance(self):
        numbers_only = NumbersOnly(Mock())
        self.assertIsInstance(numbers_only, NumbersOnly)

    def test_method_get_count_and_bonus_with_only_numbers_should_be_count_of_numbers(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='12321313')
        numbers_only = NumbersOnly(password_mock)
        self.assertEqual(8, numbers_only.get_count())
        self.assertEqual(-8, numbers_only.get_bonus())

    def test_method_get_count_and_bonus_with_not_only_numbers_should_be_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='12a21a21a')
        numbers_only = NumbersOnly(password_mock)
        self.assertEqual(0, numbers_only.get_count())
        self.assertEqual(0, numbers_only.get_bonus())
