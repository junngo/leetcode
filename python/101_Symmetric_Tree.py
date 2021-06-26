# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and \
                self.isSymmetricTree(node1.left, node2.right) and self.isSymmetricTree(node1.right, node2.left)
        else:
            return node1 == node2


if __name__ == "__main__":
    node, node.left, node.right, node.left.right = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3)
    ret = Solution().isSymmetric(node)
    print(ret)