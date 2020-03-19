import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/two")

from challenge_two import traversal_count

class TestChallenge(unittest.TestCase):

    def test(self):
        # tests are specific to system created by cloudformation
        self.assertEqual(traversal_count('/opt/yarn/bin/'), 5)
        self.assertEqual(traversal_count('/usr/share/X11/'), 191)
        self.assertEqual(traversal_count('/usr/include/X11/'), 97)


if __name__ == '__main__':
    unittest.main()
