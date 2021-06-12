# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")
        def maxend(node):
            nonlocal max_path
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            max_path = max(max_path, left + node.val + right)

            return max(node.val + max(left, right), 0)

        maxend(root)

        return max_path


if __name__ == "__main__":
    # node, node.left, node.right = TreeNode(1), TreeNode(2), TreeNode(3)
    node, node.left, node.right = TreeNode(-10), TreeNode(9), TreeNode(20)
    node.right.left, node.right.right = TreeNode(15), TreeNode(7)
    result = Solution().maxPathSum(node)
    print(result)
