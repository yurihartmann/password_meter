import unittest

from app.password.password import Password


class TestPassword(unittest.TestCase):

    def test_password_constructor_and_get_value_method_return_the_correct_value(self):
        password = Password('123abc!@#')
        self.assertEqual(password.get_value(), '123abc!@#')

