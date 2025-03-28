from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode]):
            nonlocal prev
            if node is None:
                return True
            if not dfs(node.left):
                return False
            if prev >= node.val:
                return False
            prev = node.val
            return dfs(node.right)

        prev = float('-inf')
        return dfs(root)
