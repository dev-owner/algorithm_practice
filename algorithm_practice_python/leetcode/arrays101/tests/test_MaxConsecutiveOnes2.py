from unittest import TestCase

from leetcode.arrays101.MaxConsecutiveOnes2 import MaxConsecutiveOnes2


class TestHeightChecker(TestCase):
    def test_height_checker(self):
        lst = [1, 0, 1, 1, 0]
        self.assertEqual(4, MaxConsecutiveOnes2.findMaxConsecutiveOnes(self, lst))

        lst = [0, 0, 0]
        self.assertEqual(1, MaxConsecutiveOnes2.findMaxConsecutiveOnes(self, lst))

        lst = [1, 1, 1]
        self.assertEqual(3, MaxConsecutiveOnes2.findMaxConsecutiveOnes(self, lst))

        lst = [1, 0, 1, 1, 1]
        self.assertEqual(5, MaxConsecutiveOnes2.findMaxConsecutiveOnes(self, lst))

        lst = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]
        self.assertEqual(9, MaxConsecutiveOnes2.findMaxConsecutiveOnes(self, lst))
