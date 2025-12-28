from typing import List, Optional

# Definition for a binary tree node.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        paths = []
        left_paths = self.binaryTreePaths(root.left)
        for p in left_paths:
            paths.append(root.val + '->' + p)
        right_paths = self.binaryTreePaths(root.right)
        for p in right_paths:
            paths.append(root.val + '->' + p)

        return paths