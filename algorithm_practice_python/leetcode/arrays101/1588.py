from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # sum of odd length subarray
        # get all subarray and sum odd length
        n = len(arr)
        ans = 0
        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                print(arr[j:j + i])
                ans += sum(arr[j:j + i])
        return ans


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    ans = Solution().sumOddLengthSubarrays(arr)
    print(f'{ans}, 58')
