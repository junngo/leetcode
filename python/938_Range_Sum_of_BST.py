# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
                    self.rangeSumBST(root.left, low, high) + \
                    self.rangeSumBST(root.right, low, high)


if __name__ == "__main__":
    tree, tree.left, tree.right, tree.left.left, tree.left.right, tree.right.right = \
        TreeNode(10), TreeNode(5), TreeNode(15), TreeNode(3), TreeNode(7), TreeNode(18)
    ret = Solution().rangeSumBST(tree, 7, 15)
    print(ret)
