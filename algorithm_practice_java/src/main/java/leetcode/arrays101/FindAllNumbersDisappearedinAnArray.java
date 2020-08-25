package leetcode.arrays101;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class FindAllNumbersDisappearedinAnArray {
    public static List<Integer> findDisappearedNumbers(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int abs = Math.abs(nums[i]) - 1;
            if (nums[abs] > 0) {
                nums[abs] = nums[abs] * -1;
            }
        }

        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                nums[j++] = i + 1;
            }
        }

        return Arrays.stream(nums).boxed().collect(Collectors.toList()).subList(0, j);
    }
}
