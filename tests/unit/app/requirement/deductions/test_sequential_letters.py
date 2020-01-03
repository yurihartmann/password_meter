import unittest
from unittest.mock import Mock

from app.requirement.deductions.sequential_letters import SequentialLetters


class TestSequentialLetters(unittest.TestCase):

    def test_instance(self):
        sequencial_letters = SequentialLetters(Mock())
        self.assertIsInstance(sequencial_letters, SequentialLetters)

    def test_method_get_sequential_letters_should_be_count_sequential_letters(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters._password.get_value.return_value = 'abcba1lmn2fedcba'
        self.assertEqual(2, sequencial_letters.get_sequential_letters())

    def test_method_get_sequential_reversed_letters_should_be_count_sequential_reversed_letters(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters._password.get_value.return_value = 'abcba1lmn2fedcba'
        self.assertEqual(5, sequencial_letters.get_sequential_reversed_letters())

    def test_method_get_count_should_be_return_sum_of_sequential_letter_and_reversed_sequential_letter(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters._password.get_value.return_value = 'abcba1lmn2fedcba'
        self.assertEqual(7, sequencial_letters.get_count())

    def test_method_get_count_without_sequential_letters_should_be_return_zero(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters._password.get_value.return_value = 'abdba1lun2f4dcpa'
        self.assertEqual(0, sequencial_letters.get_count())
