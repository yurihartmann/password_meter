import unittest
from unittest.mock import Mock, MagicMock

from app.rate.condition_increment import ConditionIncrement


class TestConditionIncrement(unittest.TestCase):

    def test_constructor(self):
        condition_increment = ConditionIncrement(5)
        self.assertIsInstance(condition_increment, ConditionIncrement)

    def test_pass_weight_in_contructor_and_get_by_method_should_be_return_same_value_in_constructor(self):
        condition_increment = ConditionIncrement(5)
        self.assertEqual(5, condition_increment.get_weight())

    def test_calculate_method_should_be_return_multiple_number_of_count_and_weight(self):
        requirement_mock = Mock()
        requirement_mock.get_password = MagicMock(return_value='asd123fgh456')
        requirement_mock.get_count = MagicMock(return_value=6)
        condition_increment = ConditionIncrement(2)
        self.assertEqual(12, condition_increment.calculate(requirement_mock))
