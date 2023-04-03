from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # mxn grid
        # 1-> land, 0 -> water
        # return the # of island
        # island -> surrounded by water
        # 벽도 물이다.
        # 1로 연결되어 있는 덩어리의 갯수를 찾으면 됨
        # 쭉 돌면서 1이면 DFS 시작

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '#'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    ans = Solution().numIslands(grid)
    print(f'{ans}, 1')
