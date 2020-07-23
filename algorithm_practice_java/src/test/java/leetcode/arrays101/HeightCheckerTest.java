package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

public class HeightCheckerTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{1, 1, 4, 2, 1, 3}, 3),
                Arguments.of(new int[]{5, 1, 2, 3, 4}, 5),
                Arguments.of(new int[]{1, 2, 3, 4, 5}, 0)
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void testHeightChecker(int[] nums, int expected) {
        assertThat(HeightChecker.heightChecker(nums)).isEqualTo(expected);
    }
}