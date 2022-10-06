from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()



if __name__ == '__main__':
    lst = [[1,2],[2,3],[4,2]]
    center = Solution().findCenter(lst)
    print(f'{center}, 2')
