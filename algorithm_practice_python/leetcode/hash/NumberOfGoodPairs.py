import collections
import math
from typing import List


class Solution:
    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        num_cnt = {i: nums.count(i) for i in nums}
        ans = 0
        for cnt in num_cnt.values():
            if cnt - 1:
                ans += int((cnt * (cnt - 1)) / 2)

        return ans

    def numIdenticalPairs(self, nums: List[int]) -> int:
       return int(sum(n * (n-1) / 2 for n in collections.Counter(nums).values()))


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    ans = Solution().numIdenticalPairs(nums)
    print(ans, 4)
