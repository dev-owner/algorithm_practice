class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        :param root: btree root node
        :return: is symmetric true false
        """
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val \
            and self.isMirror(left.left, right.right) \
            and self.isMirror(left.right, right.left)
