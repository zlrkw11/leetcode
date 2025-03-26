from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node:
                return True
            if node.left.val >= node.val:
                return False
            if node.right.val <= node.val:
                return False
            dfs(node.left)
            dfs(node.right)

        return True
