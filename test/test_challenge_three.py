import sys
import os
import unittest
from datetime import datetime

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/three")

from challenge_three import day_of_the_week

class TestChallenge(unittest.TestCase):

    def test(self):
        self.assertEqual(day_of_the_week(
            datetime(2019, 9, 6, 11, 33, 0)), 'Friday')
        self.assertEqual(day_of_the_week(
            datetime(2000, 12, 25, 12, 0, 0)), 'Monday')
        self.assertEqual(day_of_the_week(
            datetime(2020, 1, 1, 12, 0, 0)), 'Wednesday')


if __name__ == '__main__':
    unittest.main()
