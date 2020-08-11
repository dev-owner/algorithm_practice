from typing import List


class MaxConsecutiveOnes2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, q, l = 0, -1, 0
        for h, num in enumerate(nums):
            if num == 0:
                l = q + 1
                q = h
            ret = max(ret, h - l + 1)
        return ret
