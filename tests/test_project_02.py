import unittest
import os
# https://stackoverflow.com/questions/6677424/how-do-i-import-variable-packages-in-python-like-using-variable-variables-i


package = os.getenv('GITHUB_ACTOR')
name = f"function"

package1 = f"{package}.project_02.modules.module"

imported = getattr(__import__(package1, fromlist=[name]), name)

#imported = __import__(name1)

from imported import function

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        value = function()
        self.assertEqual(value, 1)