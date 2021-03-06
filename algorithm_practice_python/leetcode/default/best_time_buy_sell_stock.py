from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     # prices[i] = i번째날 가격
    #     # 가장 싸게 사서 비싸게 팔때 최대 이윤
    #     # 현재 위치 - 나머지 위치(n) = max를 찾아라
    #
    #     max_profit = 0
    #     min_price = float('inf')
    #     for price in prices:
    #         min_price = min(price, min_price)
    #         profit = price - min_price
    #         max_profit = max(profit, max_profit)
    #
    #     return max_profit
    def maxProfit(self, prices: List[int]) -> int:
        max_current, max_profit = 0, 0
        for idx in range(1, len(prices)):
            max_current += prices[idx] - prices[idx-1]
            max_current = max(0, max_current)
            max_profit = max(max_current, max_profit)

        return max_profit
