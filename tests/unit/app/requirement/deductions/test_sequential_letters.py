import unittest
from unittest.mock import Mock

from app.requirement.deductions.sequential_letters import SequentialLetters


class TestSequentialLetters(unittest.TestCase):

    def test_instance(self):
        sequencial_letters = SequentialLetters(Mock())
        self.assertIsInstance(sequencial_letters, SequentialLetters)

    def test_method_get_sequential_letters_should_be_count_sequential_letters(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters.password.get_value.return_value = 'abc1lmn'
        self.assertEqual(2, sequencial_letters.get_sequential_letters())

    def test_method_get_sequential_reversed_letters_should_be_count_sequential_reversed_letters(self):
        sequencial_letters = SequentialLetters(Mock())
        sequencial_letters.password.get_value.return_value = 'abcba1lmn2fedcba'
        self.assertEqual(5, sequencial_letters.get_sequential_reversed_letters())

    # ARRUMAR O SEQUENCIAL