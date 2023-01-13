from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """
            freq = nums[i*2]
            val = nums[i*2+1]
            return sum of all new list
        """
        ans = []

        for i in range(len(nums) // 2):
            freq = nums[i*2]
            val = nums[i*2+1]
            new_arr = [val] * freq
            ans.extend(new_arr)

        return ans

    def sol2(self, nums):
        return [x for a, b in zip(nums[::2], nums[1::2]) for x in [b] * a]

if __name__ == '__main__':
    nums = [1,2,3,4]
    ans = Solution().sol2(nums)
    print(f'{ans}, [2,4,4,4]')
