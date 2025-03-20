from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node == None:
                return -1
            left = height(node)
            right = height(node)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return max(left, right)+1
        return False
