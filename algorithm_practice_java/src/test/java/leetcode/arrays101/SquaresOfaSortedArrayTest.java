package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class SquaresOfaSortedArrayTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{-4, -1, 0, 3, 10}, new int[]{0, 1, 9, 16, 100})
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void testAortedSquares(int[] nums, int[] expected) {
        assertArrayEquals(expected, SquaresOfaSortedArray.sortedSquares(nums));
    }
}