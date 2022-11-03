from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return the length of the longest strictly increasing subsequence.
        # 최장 증가 부분 수열
        # 주어진 수열에서 오름차순으로 정렬된 가장 긴 부분 수열을 찾는 문제, 유일할 필요는 없다
        # 현재값이 이전값보다 작거나같으면 고르면 안되고 크면 넘어가야 한다
        # https://sskl660.tistory.com/89
        size = len(nums)
        dp = [1] * size
        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 2, 3]
    ans = Solution().lengthOfLIS(nums)
    print(f'{ans}, 4')
