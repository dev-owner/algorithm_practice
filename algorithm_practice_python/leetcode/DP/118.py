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
        """

        ans = []

        for i in range(numRows):
            for j in range(i):
                if j == 0 or j == i:
                    ans = ans + [[1]]
                else:
                    pass


        return ans
if __name__ == '__main__':
    numRows = 5
    ans = Solution().generate(numRows)
    print(f'{ans}, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]')

