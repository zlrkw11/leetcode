from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        dfs(root, ans)
        return ans

def dfs(node, ans):
    if not node:
        return None
    ans.append(node)
    if node.left and node.right:
        dfs(node.right,ans)
    if node.left and not node.right:
        dfs(node.left,ans)
