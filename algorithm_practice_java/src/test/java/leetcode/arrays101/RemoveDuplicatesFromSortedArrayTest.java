package leetcode.arrays101;

import org.junit.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import static org.junit.Assert.*;

public class RemoveDuplicatesFromSortedArrayTest {



    @ParameterizedTest
    @MethodSource("provider")
    public void testRemoveDuplicates(int[] nums) {
        RemoveDuplicatesFromSortedArray.removeDuplicates(nums);
    }
}