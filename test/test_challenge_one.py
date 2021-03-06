import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/one")

from challenge_one import odds

class TestChallenge(unittest.TestCase):

    def test(self):
        self.assertEqual(odds([0, 1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(odds(['Matt', 'Andy', 'Tom', 'Jeremy']),
                         ['Andy', 'Jeremy'])
        self.assertEqual(odds(['This', 'one', 'is', 'hidden', '.']),
                         ['one', 'hidden'])


if __name__ == '__main__':
    unittest.main()
