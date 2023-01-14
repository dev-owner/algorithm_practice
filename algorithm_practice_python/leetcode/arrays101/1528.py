from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)

        for k, v in zip(indices, s):
            ans[k] = v

        return "".join(ans)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    ans = Solution().restoreString(s, indices)
    print(f'{ans}, leetcode')
