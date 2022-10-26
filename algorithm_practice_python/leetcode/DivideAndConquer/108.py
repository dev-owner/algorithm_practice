# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:

    def helper(self, nums, low, high):
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, low, mid - 1)
        node.right = self.helper(nums, mid + 1, high)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        return self.helper(nums, 0, len(nums) - 1)

    def sortedArrayToBST_1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1:])
        )