import unittest
from unittest.mock import Mock, MagicMock

from app.requirement.additions.minimum_requirements import MinimumRequirements


class TestMinimumRequirements(unittest.TestCase):

    def test_instance(self):
        minimum_requirements = MinimumRequirements(Mock())
        self.assertIsInstance(minimum_requirements, MinimumRequirements)

    def test_method_get_count_should_be_sum_of_requirements(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aA1asdaa,')
        minimum_requirements = MinimumRequirements(password_mock)
        self.assertEqual(5, minimum_requirements.get_count())

    def test_method_get_bonus_should_be_bonus(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='bb44BBhh')
        minimum_requirements = MinimumRequirements(password_mock)
        self.assertEqual(8, minimum_requirements.get_bonus())

    def test_method_get_count_should_be_return_zero(self):
        password_mock = Mock()
        password_mock.get_value = MagicMock(return_value='aasdaa')
        minimum_requirements = MinimumRequirements(password_mock)
        self.assertEqual(0, minimum_requirements.get_count())