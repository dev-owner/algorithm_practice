from unittest import TestCase

from leetcode.BruteForce.LLN import LLN


class TestBinarySearch(TestCase):
    def test_search(self):
        n, m, k = 5, 8, 3
        N = "2 4 5 4 6"
        self.assertEqual(46, LLN.run(n, m, k, N))
