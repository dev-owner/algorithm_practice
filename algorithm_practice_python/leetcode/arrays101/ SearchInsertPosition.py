from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        for i, num in enumerate(nums):
            if num > target:
                return i

        return len(nums)


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    output = 4
    sol = Solution()
    result = sol.searchInsert(nums, target)
    print(result)
    assert result == output
