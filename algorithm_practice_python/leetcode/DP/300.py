from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return the length of the longest strictly increasing subsequence.
        # https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained/?orderBy=most_votes
        result = 0
        prev = 0
        cur_sum = 1
        for current in nums:
            if prev > current:
                result = cur_sum if cur_sum > result else result
                cur_sum = 1
            cur_sum += 1
            prev = current
        return result



if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    ans = Solution().lengthOfLIS(nums)
    print(f'{ans}, 4')
