import unittest
from unittest.mock import Mock, MagicMock

from app.rate.condition import Condition


class TestCondition(unittest.TestCase):

    def test_constructor(self):
        condition = Condition(4)
        self.assertIsInstance(condition, Condition)

    def test_pass_weight_in_contructor_and_get_by_method_should_be_return_same_value_in_constructor(self):
        condition = Condition(4)
        self.assertEqual(4, condition.get_weight())

    def test_calculate_method_should_be_return_multiple_number_of_count_and_weight(self):
        requirement_mock = Mock()
        requirement_mock.get_password = MagicMock(return_value='')
        requirement_mock.get_count = MagicMock(return_value=10)
        condition = Condition(4)
        self.assertEqual(40, condition.calculate(requirement_mock))
