from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # ans[i] = sum(nums[0]..nums[i])
        ans = []
        l = len(nums)
        for i in range(1, l + 1):
            s = 0
            for j in range(i):
                s += nums[j]
            ans.append(s)
        return ans


if __name__ == '__main__':
    nums = [1,2,3,4]
    ans = Solution().runningSum(nums)
    print(f'{ans}, [1,3,6,10]')
