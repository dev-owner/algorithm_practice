import pytest

from leetcode.google.odd_even_jump import OddEvenJump


@pytest.mark.parametrize("input, expected",
                         [([10, 13, 12, 14, 15], 2), ([2, 3, 1, 1, 4], 3), ([14, 13, 15], 3), (
                                 [1, 2, 3, 2, 1, 4, 4, 5], 6)])
def test_odd_even_jump(input, expected):
    jump = OddEvenJump()
    assert jump.oddEvenJumps(input) == expected
