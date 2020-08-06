package leetcode.arrays101;

/**
 * url : https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3230/
 */
public class MaxConsecutiveOnes2 {
    public static int findMaxConsecutiveOnes(int[] nums) {
        int max = -1;
        int cur = 0;
        int idx = 0;
        Boolean first = true;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                cur++;
            } else if (nums[i] == 0 && first) {
                cur++;
                idx = i;
                first = false;
            } else if (nums[i] == 0 && !first) {
                if (max < cur) {
                    max = cur;
                }
                cur = 0;
                first = true;
                i = idx;
            }
        }

        return (max < cur) ? cur : max;
    }
}
