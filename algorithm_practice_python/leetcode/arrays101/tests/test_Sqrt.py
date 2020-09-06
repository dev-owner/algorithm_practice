from unittest import TestCase

from leetcode.BinarySearch.Sqrt import Sqrt


class TestSqrt(TestCase):
    def test_my_sqrt(self):
        self.assertEqual(2, Sqrt.mySqrt(self, 4))
        self.assertEqual(2, Sqrt.mySqrt(self, 8))
