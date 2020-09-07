package leetcode.binary_search;

public class Sqrt {
    public static int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 2;
        int right = x / 2;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long tgt = (long)mid * mid;
            if (tgt < x) {
                left = mid + 1;
            } else if (tgt > x) {
                right = mid - 1;
            } else {
                return mid;
            }
        }

        return right;
    }
}
