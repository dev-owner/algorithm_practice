from unittest import TestCase

from leetcode.BruteForce.LLN import LLN


class TestLLN(TestCase):
    def test_basic(self):
        n, m, k = 5, 8, 3
        N = "2 4 5 4 6"
        self.assertEqual(46, LLN.basic(n, m, k, N))

    def test_advanced(self):
        n, m, k = 5, 7, 2
        N = "3 4 3 4 3"
        self.assertEqual(28, LLN.advanced(n, m, k, N))
