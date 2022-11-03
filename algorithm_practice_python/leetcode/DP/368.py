from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums.sort()
        size = len(nums)
        dp = [[num] for num in nums]
        for i in range(size):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)


if __name__ == '__main__':
    nums = [1, 2, 3]
    ans = Solution().largestDivisibleSubset(nums)
    print(f'{ans}, [1,2]')
