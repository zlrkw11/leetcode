"""
微技能 05：Matrix 基础遍历

训练点：
1) 行遍历 / 列遍历
2) 边界检查
3) 转置与旋转的索引映射
"""

from typing import List

from ._utils import run_cases


def row_sums(matrix: List[List[int]]) -> List[int]:
    """
    已实现：
    返回每一行的和。
    """
    return [sum(row) for row in matrix]


def col_sums(matrix: List[List[int]]) -> List[int]:
    """
    TODO:
    返回每一列的和。
    假设 matrix 非空且每行长度一致。
    """
    raise NotImplementedError("实现 col_sums")


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    TODO:
    返回转置矩阵。
    """
    raise NotImplementedError("实现 transpose")


def main_diagonal_sum(matrix: List[List[int]]) -> int:
    """
    TODO:
    计算主对角线元素和（仅方阵）。
    """
    raise NotImplementedError("实现 main_diagonal_sum")


def run_checks() -> None:
    sample = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    run_cases(
        "Warmup（已实现）",
        [
            ("row_sums", lambda: row_sums(sample)),
        ],
    )
    run_cases(
        "TODO 练习",
        [
            ("col_sums", lambda: col_sums(sample)),
            ("transpose", lambda: transpose(sample)),
            ("main_diagonal_sum", lambda: main_diagonal_sum(sample)),
        ],
    )
