from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        if root.left:
            l = root.left 
            total += l.val
            if total == targetSum:
                return True
            self.hasPathSum(root, targetSum)
        if root.right:
            r = root.right
            total += r.right
            if total == targetSum:
                return True
            self.hasPathSum(root, targetSum)
        return False
