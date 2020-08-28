from unittest import TestCase

from leetcode.arrays101.BinarySearch import BinarySearch


class TestBinarySearch(TestCase):
    def test_search(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(4, BinarySearch.search(nums, target))
        target = 2
        self.assertEqual(-1, BinarySearch.search(nums, target))
        nums = [5]
        target = 5
        self.assertEqual(0, BinarySearch.search(nums, target))
        nums = [2,5]
        target = 5
        self.assertEqual(1, BinarySearch.search(nums, target))
