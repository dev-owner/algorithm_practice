from unittest import TestCase

from leetcode.arrays101.ThirdMaximumNumber import ThirdMaximumNumber


class Test(TestCase):
    def test_thirdMax(self):
        arr = [3, 2, 1]
        self.assertEqual(1, ThirdMaximumNumber.thirdMax(self, arr))

        arr = [1, 2]
        self.assertEqual(2, ThirdMaximumNumber.thirdMax(self, arr))

        arr = [1, 1, 2]
        self.assertEqual(2, ThirdMaximumNumber.thirdMax(self, arr))

        arr = [2, 2, 3, 1]
        self.assertEqual(1, ThirdMaximumNumber.thirdMax(self, arr))
