import unittest
from unittest.mock import Mock

from app.requirement.additions.numbers import Numbers


class TestNumbers(unittest.TestCase):

    def test_instance(self):
        numbers = Numbers(Mock())
        self.assertIsInstance(numbers, Numbers)

    def test_method_get_count_should_be_numbers_of_numbers(self):
        numbers = Numbers(Mock())
        numbers.password.get_value.return_value = 'asd123fgh456'
        self.assertEqual(6, numbers.get_count())

    def test_method_get_bonus_with_numbers_and_letters_should_be_bonus(self):
        numbers = Numbers(Mock())
        numbers.password.get_value.return_value = '123asd456fgh'
        self.assertEqual(24, numbers.get_bonus())

    def test_method_get_bonus_with_numbers_and_without_letters_should_be_zero(self):
        numbers = Numbers(Mock())
        numbers.password.get_value.return_value = '123456'
        self.assertEqual(0, numbers.get_bonus())
