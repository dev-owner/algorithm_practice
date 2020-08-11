package leetcode.arrays101;

/**
 * url : https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3230/
 */
public class MaxConsecutiveOnes2 {
    // native solution
/*    public static int findMaxConsecutiveOnes(int[] nums) {
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
    }*/

    public static int findMaxConsecutiveOnes(int[] nums) {
        //idea : keep a window [l, h] that contains at most k zero
        //time : n sapce : 1

        int max = 0, zero = 0, k = 1; //flip at most k zero
        for (int l = 0, h = 0; h < nums.length; h++) {
            if (nums[h] == 0) {
                zero++;
            }
            while (zero > k) {
                if (nums[l++] == 0) {
                    zero--;
                }
            }
            max = Math.max(max, h - l + 1);
        }
        return max;
    }

}
