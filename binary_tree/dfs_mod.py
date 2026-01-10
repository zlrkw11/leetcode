# max, min, height, path sum, depth
def dfs(node) -> int:
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)

    return left + right + 1

