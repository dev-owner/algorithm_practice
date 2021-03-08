package leetcode.default

import kotlin.math.min
import kotlin.math.max

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var maxProfit = 0
        var minPrice = Int.MAX_VALUE
        for (price in prices) {
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)
        }
        return maxProfit
    }
}