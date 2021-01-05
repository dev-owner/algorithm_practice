from unittest import TestCase

from leetcode.BinarySearch.SearchInRotatedSortedArray import SearchInRotatedSortedArray


class TestSearchInRotatedSortedArray(TestCase):
    def test_search(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        self.assertEqual(4, SearchInRotatedSortedArray.search(self, nums, target))
