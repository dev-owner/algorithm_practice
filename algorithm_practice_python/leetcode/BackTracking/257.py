# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# backtracking
# DFS는 모든 길을 다 찾는다. 여기서 안될 것 같은 길(unpromising)은 조기 차단(pruning)해버리는게 backtracking. 일종의 최적화 기법.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # leaf node로 가는 모든 path를 찾아서 list에 넣기
        ans = []
        if not root: return ans

        def dfs(root, ans, path=""):
            if not root.left and not root.right:
                ans.append(f'{path}{root.val}')
            if root.left:
                dfs(root.left, ans, f'{path}{root.val}->')
            if root.right:
                dfs(root.right, ans, f'{path}{root.val}->')

        dfs(root, ans)
        return ans


if __name__ == '__main__':
    root = [1, 2, 3, None, 5]

    d = None
    e = TreeNode(5)
    b = TreeNode(2,d,e)
    c = TreeNode(3)
    a = TreeNode(1, b, c)



    ans = Solution().binaryTreePaths(a)
    print(f'{ans}, ["1->2->5","1->3"]')
