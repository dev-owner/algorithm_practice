package leetcode.arrays101;

/**
 * url: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
 */
public class SortArrayByParity {
    public static int[] sortArrayByParity(int[] A) {
        // even first, odd last and no matter orders
        int slow = 0;
        for (int fast = 0; fast < A.length; fast++) {
            if (A[fast] % 2 == 0) {
                int temp = A[slow];
                A[slow] = A[fast];
                A[fast] = temp;
                slow++;
            }
        }
        return A;
    }
}
