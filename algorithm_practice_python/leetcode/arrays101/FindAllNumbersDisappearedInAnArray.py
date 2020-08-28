from typing import List


class FindAllNumbersDisappearedInAnArray:
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> List[int]:
        size = len(nums) + 1
        ret = set([num for num in range(1, size)])
        nums = set(nums)
        return list(ret - nums)
