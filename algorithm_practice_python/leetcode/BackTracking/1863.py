
from functools import reduce
from itertools import chain, combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
        sum = 0
        for s in subsets:
            if s:
                sum += reduce(lambda x, y: x ^ y, s)

        return sum


if __name__ == '__main__':
    nums = [1, 3]
    ans = Solution().subsetXORSum(nums)
    print(f"{ans}, 6")
