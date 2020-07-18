from unittest import TestCase

from leetcode.arrays101.MoveZeroes import MoveZeroes


class Test(TestCase):
    def test_move_zeroes(self):
        arr = [0, 1, 0, 3, 12]
        MoveZeroes.moveZeroes(self, arr)
        self.assertEqual([1, 3, 12, 0, 0], arr)

        arr = [0, 0, 0, 1, 0, 3, 4, 0]
        MoveZeroes.moveZeroes(self, arr)
        self.assertEqual([1, 3, 4, 0, 0, 0, 0, 0], arr)

        arr = [1, 2, 0, 3, 0, 0, 4, 0]
        MoveZeroes.moveZeroes(self, arr)
        self.assertEqual([1, 2, 3, 4, 0, 0, 0, 0], arr)
