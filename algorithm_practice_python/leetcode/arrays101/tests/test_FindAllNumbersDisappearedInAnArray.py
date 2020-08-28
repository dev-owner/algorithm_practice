from unittest import TestCase

from leetcode.arrays101.FindAllNumbersDisappearedInAnArray import FindAllNumbersDisappearedInAnArray


class TestFindAllNumbersDisappearedInAnArray(TestCase):
    def test_find_disappeared_numbers(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEqual([5, 6],
                         FindAllNumbersDisappearedInAnArray.find_disappeared_numbers(nums))

        nums = [1, 1]
        self.assertEqual([2],
                         FindAllNumbersDisappearedInAnArray.find_disappeared_numbers(nums))
