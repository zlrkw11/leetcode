from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx):
            if not node:
                return
            nonlocal ans
            if node.val >= mx:
                mx = node.val
                ans += 1

            dfs(node.left,mx)
            dfs(node.right,mx)

        mx = float("-inf")
        ans = 0
        dfs(root, mx)
        return ans
