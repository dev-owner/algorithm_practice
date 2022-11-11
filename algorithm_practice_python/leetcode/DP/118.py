from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
            Pascal's Triangle
            1
            1 1
            1 2 1
            1 3 3 1
            1 4 6 4 1

            time : n^2
            space : n^2
        """
        ans = [[1] * i for i in range(1, numRows + 1)]
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]
        return ans


if __name__ == '__main__':
    numRows = 5
    ans = Solution().generate(numRows)
    print(f'{ans}, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]')
