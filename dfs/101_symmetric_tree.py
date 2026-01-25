# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curArr, node):
            if not node:
                return False
            
            else:
                curArr.append(node.left)
                curArr.append(node.right)
                dfs(curArr, node.left)
                dfs(curArr, node.right)

        print(dfs([root], root))

        
        return dfs(root)