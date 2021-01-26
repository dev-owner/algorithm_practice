import pytest

from leetcode.google.sum_of_subarray_minimums import SumOfSubarrayMinimums


@pytest.mark.parametrize("input, expected", [([3, 1, 2, 4], 17), ([11, 81, 94, 43, 3], 444)])
def test_sum_subarray_mins(input, expected):
    sum = SumOfSubarrayMinimums()
    assert sum.sumSubarrayMins(input) == expected
