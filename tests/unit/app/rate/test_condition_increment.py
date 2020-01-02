import unittest
from unittest.mock import Mock

from app.rate.condition_increment import ConditionIncrement


class TestConditionIncrement(unittest.TestCase):

    def test_constructor(self):
        condition_increment = ConditionIncrement(5)
        self.assertIsInstance(condition_increment, ConditionIncrement)

    def test_pass_weight_in_contructor_and_get_by_method(self):
        condition_increment = ConditionIncrement(5)
        self.assertEqual(5, condition_increment.get_weight())

    def test_calculate_method(self):
        requirement_mock = Mock()
        requirement_mock.password.get_value.return_value = 'asd123fgh456'
        requirement_mock.get_count.return_value = 6
        condition_increment = ConditionIncrement(2)
        self.assertEqual(12, condition_increment.calculate(requirement_mock))
