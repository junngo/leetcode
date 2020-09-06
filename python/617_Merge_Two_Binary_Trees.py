"""
Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  

Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val, t2.val)
            node.left = mergeTrees(t1.left, t2.left)
            node.right = mergeTrees(t1.right, t2.right)

            return node

        else:
            return t1 or t2


if __name__ == "__main__":
    t1, t1.right, t1.left, t1.left.left = \
        TreeNode(1), TreeNode(3), TreeNode(2), TreeNode(5)
    
    t2, t2.left, t2.right, t2.left.right, t2.right.right = \
        TreeNode(2), TreeNode(1), TreeNode(3), TreeNode(4), TreeNode(7)
    
    ret = Solution().mergeTrees(t1, t2)

