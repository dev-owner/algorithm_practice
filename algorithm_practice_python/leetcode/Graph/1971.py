from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

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


    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        visitied = [False] * n
        q = [source]
        while q:
            curr = q.pop(0)
            if curr == destination: return True
            elif curr in neighbors and not visitied[curr]:
                q.extend(neighbors[curr])
            visitied[curr] = True
        return False




if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    ans = Solution().validPath2(n, edges, source, destination)
    print(f'{ans}, true')
