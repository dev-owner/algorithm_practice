package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

public class MaxConsecutiveOnes2Test {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{1, 0, 1, 1, 0}, 4),
                Arguments.of(new int[]{0, 0, 0, 0, 0}, 1),
                Arguments.of(new int[]{1, 1, 1, 1, 1, 1}, 6),
                Arguments.of(new int[]{1, 0, 1, 1, 1}, 5),
                Arguments.of(new int[]{1, 0, 1, 1, 0, 1, 1, 1, 0, 0}, 6),
                Arguments.of(new int[]{1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1}, 9)
        );

    }

    @ParameterizedTest
    @MethodSource("provider")
    public void findMaxConsecutiveOnes(int nums[], int expected) {
        assertThat(MaxConsecutiveOnes2.findMaxConsecutiveOnes(nums)).isEqualTo(expected);
    }
}