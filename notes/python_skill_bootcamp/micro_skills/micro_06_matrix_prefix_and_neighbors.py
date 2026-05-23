"""
微技能 06：Matrix 前缀和 + 邻居遍历

训练点：
1) 二维前缀和构建
2) O(1) 子矩阵求和
3) 四方向邻居遍历（网格常用）
"""

from typing import List, Tuple

from ._utils import run_cases


def build_prefix_2d(matrix: List[List[int]]) -> List[List[int]]:
    """
    已实现：
    构建二维前缀和 prefix，尺寸为 (m+1) x (n+1)。
    """
    if not matrix or not matrix[0]:
        return [[0]]

    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        row_sum = 0
        for j in range(1, n + 1):
            row_sum += matrix[i - 1][j - 1]
            prefix[i][j] = prefix[i - 1][j] + row_sum
    return prefix


def submatrix_sum(prefix: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
    """
    TODO:
    使用 prefix 计算闭区间子矩阵 [r1..r2][c1..c2] 的和。
    """
    raise NotImplementedError("实现 submatrix_sum")


def valid_neighbors(m: int, n: int, r: int, c: int) -> List[Tuple[int, int]]:
    """
    TODO:
    返回 (r,c) 的四方向合法邻居坐标（上右下左，越界过滤）。
    """
    raise NotImplementedError("实现 valid_neighbors")


def count_value_in_grid(matrix: List[List[int]], target: int) -> int:
    """
    TODO:
    遍历整个矩阵，统计 target 出现次数。
    """
    raise NotImplementedError("实现 count_value_in_grid")


def run_checks() -> None:
    sample = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    prefix = build_prefix_2d(sample)

    run_cases(
        "Warmup（已实现）",
        [
            ("build_prefix_2d", lambda: prefix),
        ],
    )
    run_cases(
        "TODO 练习",
        [
            ("submatrix_sum", lambda: submatrix_sum(prefix, 1, 1, 2, 2)),
            ("valid_neighbors", lambda: valid_neighbors(3, 3, 1, 1)),
            ("count_value_in_grid", lambda: count_value_in_grid(sample, 5)),
        ],
    )
