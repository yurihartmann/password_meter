import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.deductions.sequential_numbers import SequentialNumbers


class TestSequentialLetters(unittest.TestCase):

    def test_instance(self):
        sequencial_numbers = SequentialNumbers(Mock())
        self.assertIsInstance(sequencial_numbers, SequentialNumbers)

    def test_method_get_sequential_numbers_should_be_count_sequential_numbers(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='123kjasbdi765lsadn6789')
        sequencial_numbers = SequentialNumbers(password_mock)
        self.assertEqual(3, sequencial_numbers.get_sequential_numbers())
        self.assertEqual(1, sequencial_numbers.get_sequential_reversed_numbers())
        self.assertEqual(4, sequencial_numbers.get_count())

    def test_method_get_count_without_sequential_letters_should_be_return_zero(self):
        sequencial_numbers = SequentialNumbers(Mock())
        sequencial_numbers._password.get_value.return_value = '163kjasbdi76d5lsa54d32d1dn67d89'
        self.assertEqual(0, sequencial_numbers.get_count())
