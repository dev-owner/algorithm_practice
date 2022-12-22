from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        ans[i] = nums[nums[i]]
        """

        return [nums[i] for i in nums]


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    ans = Solution().buildArray(nums)
    print(f'{ans}, [0,1,2,4,5,3]')
