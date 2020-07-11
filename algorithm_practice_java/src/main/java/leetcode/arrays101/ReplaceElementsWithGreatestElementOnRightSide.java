package leetcode.arrays101;


import java.util.Arrays;
import java.util.Collections;

import static com.sun.xml.internal.xsom.impl.UName.comparator;

/**
 * url: https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
 */
public class ReplaceElementsWithGreatestElementOnRightSide {
    //Failed. Time limit exceeded
    /*public static int[] replaceElements(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                arr[i] = -1;
                break;
            }
            int max = Arrays.stream(Arrays.copyOfRange(arr, i + 1, arr.length)).max().getAsInt();
            arr[i] = max;
        }
        return arr;
    }*/

    //OK. But horrible performance.
    /*public static int[] replaceElements(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                arr[i] = -1;
                break;
            }
            int max = Integer.MIN_VALUE;
            for (int j = i + 1; j < arr.length; j++) {
                if (max <= arr[j]) {
                    max = arr[j];
                }
            }
            arr[i] = max;
        }
        return arr;
    }*/

    public static int[] replaceElements(int[] arr) {
        int max = -1, n = arr.length, a;
        for (int i = n - 1; i >= 0; i--) {
            a = arr[i];
            arr[i] = max;
            max = Math.max(max, a);
        }
        return arr;
    }
}

