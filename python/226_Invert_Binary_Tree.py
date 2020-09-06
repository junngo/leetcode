"""
Invert a binary tree.

Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                
                stack.append(node.left)
                stack.append(node.right)
        
        return root



if __name__ == "__main__":
    tree, tree.left, tree.right, tree.left.left, tree.left.right, tree.right.left, tree.right.right = \
        TreeNode(4), TreeNode(2), TreeNode(7), TreeNode(1), TreeNode(3), TreeNode(6), TreeNode(9)
    ret = Solution().invertTree(tree)
