from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # dfs
        # depth first search
        # 방문 표시, 계속 파고듬
        # 인접 리스트 준비 필요
        neighbors = defaultdict(list)
        for k, v in edges:
            neighbors[k].append(v)
            neighbors[v].append(k)

        visited = set()

        def dfs(node, end):
            if node == end: return True
            if node in visited: return False
            visited.add(node)
            for neighbor in neighbors[node]:
                if dfs(neighbor, end):
                    return True
            return False

        return dfs(source, destination)


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    ans = Solution().validPath(n, edges, source, destination)
    print(f'{ans}, true')
