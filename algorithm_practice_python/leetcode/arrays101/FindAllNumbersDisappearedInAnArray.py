from typing import List


class FindAllNumbersDisappearedInAnArray:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums) + 1
        ret = set([num for num in range(1, size)])
        nums = set(nums)
        return list(ret - nums)
