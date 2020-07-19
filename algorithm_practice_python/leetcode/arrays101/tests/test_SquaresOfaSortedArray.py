from unittest import TestCase

from leetcode.arrays101.SquaresOfaSortedArray import SquaresOfaSortedArray


class Test(TestCase):
    def test_squares_ofa_sorted_array(self):
        arr = [-4, -1, 0, 3, 10]
        self.assertEqual([0, 1, 9, 16, 100], SquaresOfaSortedArray.sortedSquares(self, arr))

        arr = [0, 2]
        self.assertEqual([0, 4], SquaresOfaSortedArray.sortedSquares(self, arr))

        arr = [1, 2]
        self.assertEqual([1, 4], SquaresOfaSortedArray.sortedSquares(self, arr))
