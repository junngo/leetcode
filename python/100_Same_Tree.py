class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        elif not p or not q:
            return False

        else:
            return p.val == q.val and \
                self.recursive(p.left, q.left) and self.recursive(p.right, q.right)