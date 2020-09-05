"""
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth


if __name__ == "__main__":
    tree, tree.left, tree.right, tree.right.left, tree.right.right = \
        TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    ret = Solution().maxDepth(tree)
    print(ret)
