from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            size = len(q)
            curr_lvl = []

            for _ in range(size):
                node = q.popleft()
                curr_lvl.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                print(curr_lvl)
            
            res.append(curr_lvl)
        return res
    
