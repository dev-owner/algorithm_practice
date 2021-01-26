from itertools import combinations
from typing import List


class SumOfSubarrayMinimums:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        모든 부분집합을 찾고 각 부분집합에서 가장 작은 값의 합을 구해라
        """
        ret = 0
        mod = 1e9
        all_sub_arr = SumOfSubarrayMinimums.sub_lists(arr)
        for sub_arr in all_sub_arr:
            if sub_arr:
                ret += min(sub_arr)

        return ret % mod

    @classmethod
    def sub_lists(cls, my_list):
        subs = [[]]
        for i in range(len(my_list)):
            n = i + 1
            while n <= len(my_list):
                sub = my_list[i:n]
                subs.append(sub)
                n += 1

        return subs