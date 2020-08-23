package leetcode.arrays101;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ThirdMaximumNumber {
    // #1 remove duplicate using lambda
/*    public static int thirdMax(int[] nums) {

        List<Integer> remove_dups = Arrays.stream(nums).boxed().distinct().collect(Collectors.toList());

        if (remove_dups.size() < 3) {
            return Collections.max(remove_dups);
        }

        int k = 3;
        while (k > 1) {
            remove_dups.remove(Collections.max(remove_dups));
            k--;
        }

        return Collections.max(remove_dups);
    }*/

    /*// #2 remove duplicate using set
    public static int thirdMax(int[] nums) {

        Set<Integer> setNums = new HashSet<>();

        for (int num : nums) setNums.add(num);

        if (setNums.size() < 3) {
            return Collections.max(setNums);
        }

        setNums.remove(Collections.max(setNums));
        setNums.remove(Collections.max(setNums));
        return Collections.max(setNums);
    }*/

    // #3 remove duplicate using set and saved up to 3 in set
    public static int thirdMax(int[] nums) {
        Set<Integer> setNums = new HashSet<>();
        for (int num : nums) {
            setNums.add(num);
            if (setNums.size() > 3) {
                setNums.remove(Collections.min(setNums));
            }

        }
        if (setNums.size() == 3) {
            return Collections.min(setNums);
        }
        return Collections.max(setNums);
    }
}
