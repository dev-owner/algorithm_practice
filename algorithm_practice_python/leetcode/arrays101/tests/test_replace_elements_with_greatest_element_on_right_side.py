from unittest import TestCase

from leetcode.arrays101.ReplaceElementsWithGreatestElementOnRightSide import ReplaceElementsWithGreatestElementOnRightSide


class TestSolution(TestCase):
    def test_replace_elements(self):
        arr = [17, 18, 5, 4, 6, 1]
        self.assertEqual([18, 6, 6, 6, 1, -1], ReplaceElementsWithGreatestElementOnRightSide.replaceElements(self, arr))

        arr = [1, 2, 3]
        self.assertEqual([3, 3, -1], ReplaceElementsWithGreatestElementOnRightSide.replaceElements(self, arr))
