from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        dfs(root, 0, ans)
        return ans

def dfs(node,depth,ans):
    if node is None:
        return
    if len(ans) == depth:
        ans.append(node.val)
    dfs(node.right,depth+1,ans)
    dfs(node.left,depth+1,ans)
