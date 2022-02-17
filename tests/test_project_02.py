import unittest
import os

package = os.getenv('GITHUB_ACTOR')
name = "modules.module"


imported = getattr(__import__(package, fromlist=[name]), name)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        value = imported()
        self.assertEqual(value, 1)