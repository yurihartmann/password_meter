import unittest
from unittest.mock import Mock

from app.password.password import Password
from app.requirement.additions.number_of_characters import NumberOfCharacters


class TestNumberOfCharacters(unittest.TestCase):

    def test_instance(self):
        number_of_characters = NumberOfCharacters(Mock())
        self.assertIsInstance(number_of_characters, NumberOfCharacters)

    def test_method_get_count_should_be_numbers_fo_characters(self):
        number_of_characters = NumberOfCharacters(Mock())
        number_of_characters.password.get_value.return_value = 'asd123fgh456'
        self.assertEqual(12, number_of_characters.get_count())

    def test_method_get_bonus_should_be_bonus(self):
        number_of_characters = NumberOfCharacters(Mock())
        number_of_characters.password.get_value.return_value = 'asd123fgh456'
        self.assertEqual(48, number_of_characters.get_bonus())