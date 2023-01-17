from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
            arithmetic triplets
            1. 0 <= i < j < k < len(nums)
            2. nums[j]-nums[i] = diff
            3. nums[k]-nums[j] = diff
        """
        ans = 0
        length = len(nums)
        for i in range(length):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        return ans

    def sol2(self, nums, diff):
        seen = set(nums)
        return sum(num - diff in seen and num - diff * 2 in seen for num in seen)

if __name__ == '__main__':
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    ans = Solution().sol2(nums, diff)
    print(f'{ans}, 2')
