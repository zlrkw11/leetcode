"""
技能组合 03：前缀和 + 差分 + 二分

练习目标：
1) 把 O(n*q) 的区间求和降到 O(n+q)
2) 熟练“批量区间更新”差分套路
3) 熟练 lower_bound / 二分答案模板
"""

from typing import Callable, List, Tuple

from ._utils import run_cases


def range_sum_queries(nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """
    TODO:
    给定 nums 和多个闭区间 [l, r]，返回每个区间和。
    提示：前缀和 prefix，区间和 = prefix[r+1] - prefix[l]
    """
    raise NotImplementedError("实现 range_sum_queries")


def apply_range_additions(n: int, updates: List[Tuple[int, int, int]]) -> List[int]:
    """
    TODO:
    长度 n 的全 0 数组，执行多次区间加法：
    updates 每项为 (l, r, delta)，表示 [l, r] 都加 delta。
    返回最终数组。
    提示：差分数组 diff
    """
    raise NotImplementedError("实现 apply_range_additions")


def first_position_ge(nums: List[int], target: int) -> int:
    """
    TODO:
    返回 nums 中第一个 >= target 的下标（nums 升序）。
    若不存在，返回 len(nums)。
    """
    raise NotImplementedError("实现 first_position_ge")


def binary_search_answer(lo: int, hi: int, predicate: Callable[[int], bool]) -> int:
    """
    二分答案通用模板（已实现）：
    在 [lo, hi] 内找最小满足 predicate(mid) == True 的值。
    若都不满足，返回 hi + 1。
    """
    ans = hi + 1
    left, right = lo, hi
    while left <= right:
        mid = (left + right) // 2
        if predicate(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            (
                "binary_search_answer",
                lambda: binary_search_answer(0, 10, lambda x: x * x >= 30),
            ),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            (
                "range_sum_queries",
                lambda: range_sum_queries([3, 1, 4, 1, 5], [(0, 2), (2, 4), (1, 3)]),
            ),
            (
                "apply_range_additions",
                lambda: apply_range_additions(
                    6,
                    [
                        (0, 2, 3),
                        (1, 4, -1),
                        (3, 5, 2),
                    ],
                ),
            ),
            ("first_position_ge", lambda: first_position_ge([1, 2, 2, 4, 7], 3)),
        ],
    )
