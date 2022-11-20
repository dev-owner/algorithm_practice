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

        q = [cloned.val]

        while q:
            if q.val == target: return


        pass


if __name__ == '__main__':
    tree = [7, 4, 3, None, None, 6, 19]
    target = 3
    output = 3



    original = TreeNode(7)
    b = TreeNode(4)
    c = TreeNode(3)
    d = TreeNode(None)
    e = TreeNode(None)
    f = TreeNode(6)
    g = TreeNode(19)

    original.left(b)
    original.right(c)
    b.left(d)
    b.right(e)
    c.left(f)
    c.right(g)

    cloned = copy.deepcopy(original)

    ans = Solution().getTargetCopy(original, cloned, target)
    print(f'{ans}, {output}')
