from typing import List, Optional

# Definition for a binary tree node.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_paths(node, path, paths):
            if node:
                path += str(node.val)
                # If it's a leaf node, add the path to results
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"  # Continue the path
                    construct_paths(node.left, path, paths)
                    construct_paths(node.right, path, paths)

        res = []
        construct_paths(root, "", res)
        return res

