# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        last = TreeNode(-1)
        stack = [root]
        while stack:
            node = stack.pop()
            last.right = node
            last.left = None

            if node and node.right:
                stack.append(node.right)

            if node and node.left:
                stack.append(node.left)

            last = node


if __name__ == "__main__":
    node, node.left, node.right = TreeNode(1), TreeNode(2), TreeNode(5)
    node.left.left, node.left.right = TreeNode(3), TreeNode(4)
    node.right.right = TreeNode(6)

    ret = Solution().flatten(node)
    print("{0} -> {1} -> {2} -> {3} -> {4} -> {5}".format(
        node.val,
        node.right.val,
        node.right.right.val,
        node.right.right.right.val,
        node.right.right.right.right.val,
        node.right.right.right.right.right.val,
    ))
