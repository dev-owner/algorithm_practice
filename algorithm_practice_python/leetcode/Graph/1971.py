from collections import defaultdict, deque
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

        visited = [False] * n

        def dfs(node, end):
            if node == end: return True
            if visited[node]: return False
            visited[node] = True
            for neighbor in neighbors[node]:
                if dfs(neighbor, end):
                    return True
            return False

        return dfs(source, destination)

    def validPath_2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # bfs
        # breadth first search
        # Queue

        if n == 1: return True

        neighbors = defaultdict(list)
        for k, v in edges:
            neighbors[k].append(v)
            neighbors[v].append(k)

        q = deque()
        q.append(source)
        visited = [False] * n

        while q:
            curr = q.popleft()
            if destination == curr: return True
            visited[curr] = True
            for n in neighbors[curr]:
                if not visited[n]:
                    q.append(n)

        return False


if __name__ == '__main__':
    n = 10
    edges = [[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]]
    source = 1
    destination = 0
    ans = Solution().validPath_2(n, edges, source, destination)
    print(f'{ans}, false')
