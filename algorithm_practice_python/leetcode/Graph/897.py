# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, nxt=None) -> TreeNode:
        # in-place re-arrange

        if not root: return nxt
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, nxt)
        return res

    def increasingBST_2(self, root):
        if not root: return None

        stack = []
        temp = x = root
        i = 0
        while stack or temp:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                node = stack.pop()
                if i==0:
                    root = x = node
                    i += 1
                else:
                    x.right = node
                    x = node
                    x.left = None
                temp = node.right
        return root




if __name__ == '__main__':
    l = TreeNode(1)
    r = TreeNode(7)
    root = TreeNode(5, l, r)


    ans = Solution().increasingBST(root)
    print(f'{ans}, ')
