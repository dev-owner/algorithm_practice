package leetcode.arrays101;

/**
 * url: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
 */
public class MoveZeroes {
    public static void moveZeroes(int[] nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                int temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
                slow++;
            }
        }
    }
}
