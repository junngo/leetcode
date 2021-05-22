# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_bst(node, left, right):
            if not node:
                return True
            
            if not left < node.val < right:
                return False

            return (check_bst(node.left, left, node.val)
                and check_bst(node.right, node.val, right))

        return check_bst(root, -math.inf, math.inf)


if __name__ == "__main__":
    node, node.left, node.right = TreeNode(2), TreeNode(1), TreeNode(3)
    ret = Solution().isValidBST(node)
    print(ret)
