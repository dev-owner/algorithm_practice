# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None

        # if same level, add
        # return new tree

        if root1.val and root2.val:
            root3.val = root1.val + root2.val



if __name__ == '__main__':


    ans = Solution().mergeTrees()
    print(f'{ans}, ')
