import unittest
from unittest.mock import patch, Mock

from app.requirement.requirement import Requirement


class TestRequirement(unittest.TestCase):

    @patch.object(Requirement, '__abstractmethods__', set())
    def test_constructor(self):
        requirement = Requirement(Mock(), Mock())
        self.assertIsInstance(requirement, Requirement)


