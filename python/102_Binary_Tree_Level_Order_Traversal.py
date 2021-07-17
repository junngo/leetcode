# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        while queue:
            cur_elements, cnt = [], len(queue)
            for i in range(cnt):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                cur_elements.append(node.val)

            result.append(cur_elements)

        return result


if __name__ == "__main__":
    node, node.left, node.right, node.right.left, node.right.right = \
        TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    ret = Solution().isSymmetric(node)
    print(ret)