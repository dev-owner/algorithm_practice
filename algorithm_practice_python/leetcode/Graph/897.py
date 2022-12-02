# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # in-place re-arrange

        pass


if __name__ == '__main__':
    l = TreeNode(1)
    r = TreeNode(7)
    root = TreeNode(5, l, r)

    ans = Solution().increasingBST(root)
    print(f'{ans}, ')
