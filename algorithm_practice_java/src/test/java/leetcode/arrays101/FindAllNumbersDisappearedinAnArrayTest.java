package leetcode.arrays101;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

public class FindAllNumbersDisappearedinAnArrayTest {

    public static Stream<Arguments> provider() {
        return Stream.of(
                Arguments.of(new int[]{4, 3, 2, 7, 8, 2, 3, 1}, new ArrayList<Integer>(Arrays.asList(5, 6))),
                Arguments.of(new int[]{2, 2}, new ArrayList<Integer>(Arrays.asList(1)))
        );
    }

    @ParameterizedTest
    @MethodSource("provider")
    public void findDisappearedNumbers(int[] nums, List<Integer> ans) {
        assertThat(FindAllNumbersDisappearedinAnArray.findDisappearedNumbers(nums)).isEqualTo(ans);
    }
}