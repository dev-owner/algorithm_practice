from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, j in zip(nums, index):
            ans.insert(j, i)
        return ans


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    ans = Solution().createTargetArray(nums,index)

    print(f'{ans}, [0,4,1,3,2]')
