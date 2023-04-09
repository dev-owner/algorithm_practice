from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers -> sorted
        # 1 <= index1 < index2 <= numbers.length
        # [index1, index2]
        hm = dict()
        for i, n in enumerate(numbers):
            if target - n in hm:
                return [hm[target - n] + 1, i + 1]
            hm[n] = i

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    ans = Solution().twoSum2(numbers, target)
    print(f'{ans}, [1,2]')
