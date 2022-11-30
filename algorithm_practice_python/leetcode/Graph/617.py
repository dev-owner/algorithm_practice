# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 and root2:
            ans = TreeNode(root1.val + root2.val)
            ans.left = self.mergeTrees(root1.left, root2.left)
            ans.right = self.mergeTrees(root1.right, root2.right)
            return ans
        else:
            return root1 or root2




if __name__ == '__main__':


    r14 = TreeNode(5)
    r13= TreeNode(2)
    r12 = TreeNode(3, r14)
    r11 = TreeNode(1, r12, r13)

    r24 = None
    r25 = TreeNode(4)
    r22 = TreeNode(1, r24, r25)
    r26 = None
    r27 = TreeNode(7)
    r23 = TreeNode(3, r26, r27)
    r21 = TreeNode(2, r22, r23)




    ans = Solution().mergeTrees(r11, r21)
    print(f'{ans}, ')
