import unittest
from unittest.mock import Mock

from app.password.password import Password
from app.rate.condition import Condition


class TestCondition(unittest.TestCase):

    def test_constructor(self):
        condition = Condition(4)
        self.assertIsInstance(condition, Condition)

    def test_pass_weight_in_contructor_and_get_by_method(self):
        condition = Condition(4)
        self.assertEqual(4, condition.get_weight())

    def test_calculate_method(self):
        requirement_mock = Mock()
        requirement_mock.password = Password('asd123fgh456')
        requirement_mock.get_count.return_value = 10
        condition = Condition(4)
        self.assertEqual(40, condition.calculate(requirement_mock))