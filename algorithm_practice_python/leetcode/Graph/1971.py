from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
            dfs
        """

        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        print(edges)

        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            seen.add(node)
            for n in neighbors[node]:
                if dfs(n, end, seen):
                    return True
            return False

        seen = set()
        return dfs(source, destination, seen)




if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    ans = Solution().validPath(n, edges, source, destination)
    print(f'{ans}, true')
