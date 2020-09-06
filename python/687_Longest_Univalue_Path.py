"""
Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    results: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.results = max(self.results, left+right)
            return max(left, right)

        dfs(root)
        return self.results


if __name__ == "__main__":
    tree, tree.left, tree.right, tree.left.left, tree.left.right, tree.right.right = \
        TreeNode(5), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(1), TreeNode(5)
    ret = Solution().longestUnivaluePath(tree)
    print(ret)
