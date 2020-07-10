package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.Assert.assertArrayEquals;

class ReplaceElementsWithGreatestElementOnRightSideTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of((Object) new int[]{17, 18, 5, 4, 6, 1}, (Object) new int[]{18, 6, 6, 6, 1, -1}),
                Arguments.of((Object) new int[]{1, 2, 3}, (Object) new int[]{3, 3, -1}),
                Arguments.of((Object) new int[]{1, 2, 3}, (Object) new int[]{3, 3, -1})
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    void replaceElements(int[] input, int[] expectedValue) {
        int[] ints = ReplaceElementsWithGreatestElementOnRightSide.replaceElements(input);
        assertArrayEquals(expectedValue, ints);
    }
}