import pytest

from leetcode.default.best_time_buy_sell_stock import Solution


@pytest.mark.parametrize("prices, expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)])
def test_max_profit(prices, expected):
    assert Solution().maxProfit(prices) == expected
