package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;

public class RemoveDuplicatesFromSortedArrayTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{1, 1, 2}, 2),
                Arguments.of(new int[]{0, 1, 2, 3}, 4),
                Arguments.of(new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}, 5)
        );

    }


    @ParameterizedTest
    @MethodSource("provider")
    public void testRemoveDuplicates(int[] nums, int expected) {
        assertEquals(expected, RemoveDuplicatesFromSortedArray.removeDuplicates(nums));
    }
}