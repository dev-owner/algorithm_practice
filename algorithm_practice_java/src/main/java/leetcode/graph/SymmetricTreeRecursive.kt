package leetcode.graph

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

//class TreeNode(var `val`: Int) {
//    var left: TreeNode? = null
//    var right: TreeNode? = null
//}

class SymmetricTreeRecursive {
    fun isSymmetric(root: TreeNode?): Boolean {
        return isMirror(root, root)
    }

    fun isMirror(left: TreeNode?, right: TreeNode?): Boolean {
        if (left == null && right == null) {
            return true
        }
        return left?.`val` == right?.`val`
                && isMirror(left?.left, right?.right)
                && isMirror(left?.right, right?.left)
    }
}