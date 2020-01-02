import unittest
from unittest.mock import Mock

from app.rate.flat_rate import FlatRate


class TestFlatRate(unittest.TestCase):

    def test_constructor(self):
        flat_rate = FlatRate(4)
        self.assertIsInstance(flat_rate, FlatRate)

    def test_pass_weight_in_contructor_and_get_by_method(self):
        flat_rate = FlatRate(2)
        self.assertEqual(flat_rate.get_weight(), 2)

    def test_calculate_method(self):
        requirement_mock = Mock()
        requirement_mock.get_count.return_value = 5
        flat_rate = FlatRate(2)
        self.assertEqual(10, flat_rate.calculate(requirement_mock))
