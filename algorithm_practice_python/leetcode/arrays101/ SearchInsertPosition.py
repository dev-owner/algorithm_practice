import bisect
import math
from typing import List


class Solution:
    def searchInsert_old(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        for i, num in enumerate(nums):
            if num > target:
                return i

        return len(nums)

    def searchInsert_bi(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    output = 4
    sol = Solution()
    result = sol.searchInsert(nums, target)
    print(result)
    assert result == output
