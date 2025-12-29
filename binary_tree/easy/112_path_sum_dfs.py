
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if self.dfs(root, 0) == False:
            return False
        if self.dfs(root, 0) == targetSum:
            return True
        return False

    
    def dfs(self, node, s):
        if not node:
            return 0
        if not node.left and not node.right:
            return False
        if node.left:
            self.dfs(node.left, s+1)

        if node.right:
            self.dfs(node.right, s+1)
        return 0
