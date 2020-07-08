package leetcode.arrays101;

/**
 * url: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
 */
public class ValidMountainArray {
    public static boolean run(int[] A) {
        int N = A.length;
        int i = 0;

        //walk up
        while (i < N-1 && A[i] < A[i+1]) {
            i++;
        }

        //peak can't be first or last
        if (i == 0 || i == N - 1) {
            return false;
        }

        //walk down
        while(i < N-1 && A[i] > A[i+1]) {
            i++;
        }

        return i == N-1;
    }
}

