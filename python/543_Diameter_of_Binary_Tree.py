"""
Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
 
            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest

    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     self.longest = 1
    #     def depth(node):
    #         if not node: 
    #             return 0

    #         L = depth(node.left)
    #         R = depth(node.right)

    #         self.longest = max(self.longest, L+R+1)
    #         return max(L, R) + 1

    #     depth(root)
    #     return self.longest - 1


if __name__ == "__main__":
    tree, tree.left, tree.right, tree.right.right, tree.left.left, tree.left.right = \
        TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(6), TreeNode(4), TreeNode(5)
    ret = Solution().diameterOfBinaryTree(tree)
    print(ret)
