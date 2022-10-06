from typing import List


class Solution:
    def findCenter_1(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

    def findCenter(self, edges: List[List[int]]) -> int:
        # e[0] vs e[1]
        return edges[0][edges[0][1] in edges[1]]


if __name__ == '__main__':
    lst = [[1,2],[2,3],[4,2]]
    center = Solution().findCenter(lst)
    print(f'{center}, 2')
