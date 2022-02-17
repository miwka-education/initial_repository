import unittest
import os

package = os.getenv('GITHUB_ACTOR')
name = "project_02.modules.module"


#imported = getattr(__import__(package, fromlist=[name]), name)

name1 = f"{package}.project_02.modules.module"
imported = __import__(name1)

from imported import function

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        value = function()
        self.assertEqual(value, 1)