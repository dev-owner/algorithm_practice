package leetcode.graph

import java.util.*

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
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) {
            return false
        }
        val arr = Stack<Pair<TreeNode, TreeNode>>()
        arr.push(Pair(root.left, root.right))
        while (arr.empty() != true) {
            val cur = arr.pop()
            val left = cur.first
            val right = cur.second

            if (left == null && right == null) {
                continue
            }

            if (left == null || right == null) {
                return false
            }

            if (left.`val` == right.`val`) {
                arr.push(Pair(left.left, right.right))
                arr.push(Pair(left.right, right.left))
            } else {
                return false
            }
        }
        return true
    }
}