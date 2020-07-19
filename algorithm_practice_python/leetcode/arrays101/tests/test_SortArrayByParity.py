from unittest import TestCase
from leetcode.arrays101.SortArrayByParity import SortArrayByParity

class Test(TestCase):
    def test_move_zeroes(self):
        arr = [3,1,2,4]

        self.assertEqual([2,4,3,1], SortArrayByParity.sortArrayByParity(self, arr))
