# Definition for a binary tree node.
import copy
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return None
            if node.val == target.val: return node

            left = dfs(node.left)
            if left: return left

            right = dfs(node.right)
            if right: return right

            return None
        return dfs(cloned)


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)


    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    ans = Solution().getTargetCopy(a, copy.deepcopy(a), e)
    print(ans)
