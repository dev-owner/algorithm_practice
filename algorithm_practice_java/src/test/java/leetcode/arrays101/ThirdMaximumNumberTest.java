package leetcode.arrays101;


import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

public class ThirdMaximumNumberTest {

    public static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{3, 2, 1}, 1),
                Arguments.of(new int[]{1, 2}, 2),
                Arguments.of(new int[]{2, 2, 3, 1}, 1)
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void testThirdMax(int[] nums, int expected) {
        assertThat(ThirdMaximumNumber.thirdMax(nums)).isEqualTo(expected);
    }

}