import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.deductions.sequential_letters import SequentialLetters


class TestSequentialLetters(unittest.TestCase):

    def test_instance(self):
        sequencial_letters = SequentialLetters(Mock())
        self.assertIsInstance(sequencial_letters, SequentialLetters)

    def test_method_get_sequential_letters_should_be_count_sequential_letters(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='abcba1lmn2fedcba')
        sequencial_letters = SequentialLetters(password_mock)
        self.assertEqual(2, sequencial_letters.get_sequential_letters())
        self.assertEqual(5, sequencial_letters.get_sequential_reversed_letters())
        self.assertEqual(7, sequencial_letters.get_count())

    def test_method_get_count_without_sequential_letters_should_be_return_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='abdba1lun2f4dcpa')
        sequencial_letters = SequentialLetters(password_mock)
        self.assertEqual(0, sequencial_letters.get_count())
