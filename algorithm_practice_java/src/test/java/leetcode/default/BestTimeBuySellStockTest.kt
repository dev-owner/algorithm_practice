package leetcode.default

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.util.stream.Stream

internal class BestTimeBuySellStockTest {

    companion object {
        @JvmStatic
        fun provider(): Stream<Arguments?>? {
            return Stream.of(
                Arguments.of(intArrayOf(7, 1, 5, 3, 6, 4), 5),
                Arguments.of(intArrayOf(7, 6, 4, 3, 1), 0)
            )
        }
    }

    @ParameterizedTest
    @MethodSource("provider")
    fun maxProfitTest(input: IntArray, expected: Int) {
        val result = Solution().maxProfit(input)
        assertThat(result).isEqualTo(expected)
    }

}

