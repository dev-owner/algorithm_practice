package leetcode.binary_search;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

public class BinarySearchTest {

    public static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{-1,0,3,5,9,12}, 9, 4),
                Arguments.of(new int[]{-1,0,3,5,9,12}, 2, -1),
                Arguments.of(new int[]{5}, 5, 0),
                Arguments.of(new int[]{2,5}, 5, 1)
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void test_search(int[] nums, int target, int ans) {
        assertThat(ans).isEqualTo(BinarySearch.search(nums, target));
    }

}