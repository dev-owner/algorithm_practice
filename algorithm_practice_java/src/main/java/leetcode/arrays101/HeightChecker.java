package leetcode.arrays101;

import java.util.Arrays;

/**
 * url : https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/
 */
public class HeightChecker {
    public static int heightChecker(int[] heights) {
        int ret = 0;
        int[] copied = heights.clone();
        Arrays.sort(heights);

        for (int i = 0; i < heights.length; i++) {
            if (copied[i] != heights[i]) {
                ret++;
            }
        }
        return ret;
    }
}
