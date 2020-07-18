package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.Assert.assertArrayEquals;

public class MoveZeroesTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of((Object) new int[]{0, 1, 0, 3, 12}, new int[]{1, 3, 12, 0, 0}),
                Arguments.of((Object) new int[]{0, 0, 0, 0}, new int[]{0, 0, 0, 0}),
                Arguments.of((Object) new int[]{0, 1, 0, 0, 2, 6}, new int[]{1, 2, 6, 0, 0, 0}),
                Arguments.of((Object) new int[]{1, 2, 0, 3, 0, 0, 4, 0, 0, 0, 5}, new int[]{1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0})
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void testMoveZeroes(int[] nums, int[] expected) {
        MoveZeroes.moveZeroes(nums);
        assertArrayEquals(expected, nums);
    }
}