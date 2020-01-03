import unittest
from unittest.mock import Mock

from app.requirement.additions.minimum_requirements import MinimumRequirements


class TestMinimumRequirements(unittest.TestCase):

    def test_instance(self):
        minimum_requirements = MinimumRequirements(Mock())
        self.assertIsInstance(minimum_requirements, MinimumRequirements)

    def test_method_get_count_should_be_sum_of_requirements(self):
        minimum_requirements = MinimumRequirements(Mock())
        minimum_requirements.password.get_value.return_value = 'aA1asdaa,'
        self.assertEqual(5, minimum_requirements.get_count())

    def test_method_get_bonus_should_be_bonus(self):
        minimum_requirements = MinimumRequirements(Mock())
        minimum_requirements.password.get_value.return_value = 'bb44BBhh'
        self.assertEqual(8, minimum_requirements.get_bonus())

    def test_method_get_count_should_be_return_zero(self):
        minimum_requirements = MinimumRequirements(Mock())
        minimum_requirements.password.get_value.return_value = 'aasdaa'
        self.assertEqual(0, minimum_requirements.get_count())