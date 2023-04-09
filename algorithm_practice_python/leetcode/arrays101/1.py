from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # <=10000
        # nlogn
        # 2개 더해서 target이 되어야 함
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(i,j)
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, n in enumerate(nums):
            if target - n in hm:
                return [hm[target-n], i]
            else:
                hm[n] = i


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    ans = Solution().twoSum2(nums, target)
    print(f'{ans}, [1,2]')
