package leetcode.default

import kotlin.math.max

class Solution {
    //    fun maxProfit(prices: IntArray): Int {
//        var maxProfit = 0
//        var minPrice = Int.MAX_VALUE
//        for (price in prices) {
//            minPrice = min(price, minPrice)
//            maxProfit = max(price - minPrice, maxProfit)
//        }
//        return maxProfit
//    }
    //using kadane's algorithm
    // maxcur += max(0, price[i]- price[i-1])
    fun maxProfit(prices: IntArray): Int {
        var maxCur = 0
        var maxSoFar = 0

        (1 until prices.size).forEach {
            maxCur += prices[it] - prices[it - 1]
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)
        }

        return maxSoFar
    }
}