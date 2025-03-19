from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.min_depth = 0
        self.max_depth = 0
        def dfs_max(node):
            if not node:
                return 0
            left = dfs_max(node.left)
            right = dfs_max(node.right)
            self.max_depth = max(left,right,self.max_depth)
            return max(left, right)+1

        def dfs_min(node):
            if not node:
                return 0
            left = dfs_max(node.left)
            right = dfs_max(node.right)
            self.min_depth = min(left,right,self.min_depth)
            return min(left, right)+1

        dfs_max(root)
        dfs_min(root)
        return self.max_depth - self.min_depth>1
