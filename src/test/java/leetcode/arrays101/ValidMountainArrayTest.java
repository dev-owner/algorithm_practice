package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class ValidMountainArrayTest {

    private static Stream<Arguments> successCaseProvider() {
        return Stream.of(
                Arguments.of((Object) new int[]{1, 2, 3, 2, 1}),
                Arguments.of((Object) new int[]{1, 5, 3}),
                Arguments.of((Object) new int[]{1, 2, 3, 4, 3, 2, 1}),
                Arguments.of((Object) new int[]{0, 3, 2, 1})
        );
    }

    @ParameterizedTest
    @MethodSource("successCaseProvider")
    public void success_validaMountainArray(int[] arr) {
        assertTrue(ValidMountainArray.run(arr));
    }

    private static Stream<Arguments> failedCaseProvider() {
        return Stream.of(
                Arguments.of((Object) new int[]{1, 2, 3}),
                Arguments.of((Object) new int[]{1, 5, 5}),
                Arguments.of((Object) new int[]{2, 1})
        );
    }

    @ParameterizedTest
    @MethodSource("failedCaseProvider")
    public void failed_validaMountainArray(int[] arr) {
        assertFalse(ValidMountainArray.run(arr));
    }
}