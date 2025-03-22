from typing import Optional
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return bfs(root)

def bfs(node):
    if not node:
        return []
    ans = []
    q = deque([node])
    while q:
        lvl = []
        for _ in range(len(q)):
            node = q.popleft()
            lvl.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(lvl)
    return ans
