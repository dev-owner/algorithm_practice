from unittest import TestCase

from leetcode.arrays101.HeightChecker import HeightChecker


class TestHeightChecker(TestCase):
    def test_height_checker(self):
        lst = [1, 1, 4, 2, 1, 3]
        self.assertEqual(3, HeightChecker.heightChecker(self, lst))

        lst = [5, 1, 2, 3, 4]
        self.assertEqual(5, HeightChecker.heightChecker(self, lst))

        lst = [1, 2, 3, 4, 5]
        self.assertEqual(0, HeightChecker.heightChecker(self, lst))
