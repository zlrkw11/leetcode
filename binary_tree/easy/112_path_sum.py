from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.left:
            l = root.left 
            targetSum -= l.val
            if targetSum == 0:
                return True
            self.hasPathSum(root.left, targetSum)
        if root.right:
            r = root.right
            targetSum -= r.val
            if targetSum == 0:
                return True
            self.hasPathSum(root.right, targetSum)
