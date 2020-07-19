package leetcode.arrays101;

import org.junit.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.Assert.*;

public class SortArrayByParityTest {

    private static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of((Object) new int[]{3,1,2,4}, new int[]{2,4,3,1})
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void testSortArrayByParity(int[] nums, int[] expected) {
        assertArrayEquals(expected,SortArrayByParity.sortArrayByParity(nums));
    }
}