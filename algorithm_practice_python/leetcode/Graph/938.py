# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        sum = 0
        if root.val > low:
            sum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)

        if low <= root.val <= high: sum += root.val

        return sum


if __name__ == '__main__':
    root = [10, 5, 15, 3, 7, None, 18]
    low = 7
    high = 15

    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(15)
    d = TreeNode(3)
    e = TreeNode(7)
    f = None
    g = TreeNode(18)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    ans = Solution().rangeSumBST(a, low, high)
    print(ans)
