from typing import List


class BinarySearch:
    @staticmethod
    def search(nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1
