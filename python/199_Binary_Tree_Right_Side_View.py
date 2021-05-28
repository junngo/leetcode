import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        deque = collections.deque()
        if root:
            deque.append(root)

        result = []
        while deque:
            size, val = len(deque), 0
            for _ in range(size):
                node = deque.popleft()
                val = node.val
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            result.append(val)

        return result


if __name__ == "__main__":
    node, node.left, node.right = TreeNode(1), TreeNode(2), TreeNode(3)
    node.left.right, node.right.right = TreeNode(5), TreeNode(4)

    # node, node.right = TreeNode(1), TreeNode(3)

    result = Solution().rightSideView(node)
    for i in result:
        print(i)
