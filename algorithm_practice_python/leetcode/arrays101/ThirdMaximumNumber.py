from typing import List


class ThirdMaximumNumber:
    # first try
    # def thirdMax(self, nums: List[int]) -> int:
    #     maximums = set()
    #     for num in nums:
    #         maximums.add(num)
    #         if len(maximums) > 3:
    #             maximums.remove(min(maximums))
    #     if len(maximums) == 3:
    #         return min(maximums)
    #     return max(maximums)

    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)

        if len(nums) < 3:
            return max(nums)

        k = 3
        while k > 1:
            nums.remove(max(nums))
            k = k - 1

        return max(nums)