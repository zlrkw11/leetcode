"""
技能组合 05：图搜索 + 回溯

练习目标：
1) 熟练邻接表建图
2) 熟练 BFS/DFS 模板
3) 熟练回溯的“做选择 -> 递归 -> 撤销选择”
"""

from collections import deque
from typing import Dict, List, Set, Tuple

from ._utils import run_cases


def count_connected_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    TODO:
    n 个点（0..n-1）和无向边 edges，返回连通分量个数。
    """
    raise NotImplementedError("实现 count_connected_components")


def shortest_path_length(
    n: int, edges: List[Tuple[int, int]], start: int, target: int
) -> int:
    """
    TODO:
    无权无向图最短路径长度，不可达返回 -1。
    提示：BFS。
    """
    raise NotImplementedError("实现 shortest_path_length")


def generate_permutations_unique(nums: List[int]) -> List[List[int]]:
    """
    TODO:
    可能包含重复元素，返回不重复的全排列。
    提示：先排序 + used 数组 + 同层去重。
    """
    raise NotImplementedError("实现 generate_permutations_unique")


def level_order_from_edges(n: int, edges: List[Tuple[int, int]], root: int) -> List[List[int]]:
    """
    练习 BFS 层序遍历（已实现）：
    输入是无向边，按层输出节点列表。
    """
    graph: Dict[int, List[int]] = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited: Set[int] = {root}
    q = deque([root])
    levels: List[List[int]] = []

    while q:
        level_size = len(q)
        level: List[int] = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node)
            for nxt in graph[node]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                q.append(nxt)
        levels.append(level)

    return levels


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            (
                "level_order_from_edges",
                lambda: level_order_from_edges(
                    6,
                    [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)],
                    0,
                ),
            ),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            (
                "count_connected_components",
                lambda: count_connected_components(6, [(0, 1), (1, 2), (3, 4)]),
            ),
            (
                "shortest_path_length",
                lambda: shortest_path_length(
                    7,
                    [(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 3)],
                    0,
                    3,
                ),
            ),
            (
                "generate_permutations_unique",
                lambda: generate_permutations_unique([1, 1, 2]),
            ),
        ],
    )


if __name__ == "__main__":
    run_checks()
