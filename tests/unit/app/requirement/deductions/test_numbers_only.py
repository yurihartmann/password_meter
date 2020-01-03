import unittest
from unittest.mock import Mock

from app.requirement.deductions.numbers_only import NumbersOnly


class TestNumbersOnly(unittest.TestCase):

    def test_instance(self):
        numbers_only = NumbersOnly(Mock())
        self.assertIsInstance(numbers_only, NumbersOnly)

    def test_method_get_count_with_only_numbers_should_be_count_of_numbers(self):
        numbers_only = NumbersOnly(Mock())
        numbers_only._password.get_value.return_value = '12321313'
        self.assertEqual(8, numbers_only.get_count())

    def test_method_get_count_with_not_only_numbers_should_be_zero(self):
        numbers_only = NumbersOnly(Mock())
        numbers_only._password.get_value.return_value = '12a21a21a'
        self.assertEqual(0, numbers_only.get_count())

    def test_method_get_bonus_with_only_numbers_should_be_count_of_numbers(self):
        numbers_only = NumbersOnly(Mock())
        numbers_only._password.get_value.return_value = '12321313'
        self.assertEqual(-8, numbers_only.get_bonus())

    def test_method_get_bonus_with_not_only_numbers_should_be_zero(self):
        numbers_only = NumbersOnly(Mock())
        numbers_only._password.get_value.return_value = '12a21a21a'
        self.assertEqual(0, numbers_only.get_bonus())