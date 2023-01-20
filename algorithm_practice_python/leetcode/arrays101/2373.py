from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
            (n-2) x (n-2) largest local matrix를 찾는 것
            3x3을 계속 이동해가면서 가장 큰 수
            [0,0], [0,1], [0,2]
            [1,0], [1,1], [1,2]
            [2,0], [2,1], [2,2]

            [0,1], [0,2], [0,3]
            [1,1], [1,2], [1,3]
            [2,1], [2,2], [2,3]

            [1,0], [1,1], [1,2]
            [2,0], [2,1], [2,2]
            [3,0], [3,1], [3,2]



        """
        """
        Time:   O(n^2)
        Memory: O(1)
        """

        def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
            n = len(grid)
            return [[self.local_max(grid, r, c, 1) for c in range(1, n - 1)] for r in range(1, n - 1)]

        @staticmethod
        def local_max(grid: List[List[int]], row: int, col: int, radius: int) -> int:
            return max(
                grid[r][c]
                for r in range(row - radius, row + radius + 1)
                for c in range(col - radius, col + radius + 1)
            )


if __name__ == '__main__':
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    ans = Solution().largestLocal(grid)
    print(f'{ans}, [[9,9],[8,6]]')
