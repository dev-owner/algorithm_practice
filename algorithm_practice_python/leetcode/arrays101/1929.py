from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

if __name__ == '__main__':
    nums = [1, 2, 1]
    ans = Solution().getConcatenation(nums)
    print(f'{ans}, [1,2,1,1,2,1]')
