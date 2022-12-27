from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # max(sum(inner list))
        return max([sum(i) for i in accounts])

    def sol(self,acc):
        return max(map(sum, acc))


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    ans = Solution().sol(accounts)
    print(f'{ans}, 6')
