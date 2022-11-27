# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return False

        if root.val in [0, 1]:
            return True if root.val else False
        else:
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            if root.val == 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)


if __name__ == '__main__':
    """
    root = full binary tree
    0 = false, 1 = true
    2 = OR , 3 = AND
    """

    d = TreeNode(val=None)
    e = TreeNode(val=None)
    f = TreeNode(0)
    g = TreeNode(1)
    c = TreeNode(3, f, g)
    b = TreeNode(1, d, e)
    a = TreeNode(2, b, c)

    ans = Solution().evaluateTree(a)
    print(f'{ans}, ')
