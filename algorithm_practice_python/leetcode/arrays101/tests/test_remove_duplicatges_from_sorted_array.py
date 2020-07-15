from unittest import TestCase

from leetcode.arrays101.RemoveDuplicatesFromSortedArray import RemoveDuplicatesFromSortedArray


class TestSolution(TestCase):
    def test_replace_elements(self):
        arr = [1, 1, 2]
        self.assertEqual(2, RemoveDuplicatesFromSortedArray.removeDuplicates(self, arr))

        arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, RemoveDuplicatesFromSortedArray.removeDuplicates(self, arr))
