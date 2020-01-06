import unittest
from unittest.mock import Mock, MagicMock

from app.password.password import Password
from app.requirement.additions.number_of_characters import NumberOfCharacters


class TestNumberOfCharacters(unittest.TestCase):

    def setUp(self) -> None:
        self.password_mock = Mock()
        self.password_mock.get_value = MagicMock(return_value='asd123fgh456')
        self.number_of_characters = NumberOfCharacters(self.password_mock)

    def test_instance(self):
        self.assertIsInstance(self.number_of_characters, NumberOfCharacters)

    def test_method_get_count_should_be_numbers_fo_characters(self):
        self.assertEqual(12, self.number_of_characters.get_count())

    def test_method_get_bonus_should_be_bonus(self):
        self.assertEqual(48, self.number_of_characters.get_bonus())