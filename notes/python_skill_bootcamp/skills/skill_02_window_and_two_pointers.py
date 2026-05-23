"""
技能组合 02：双指针 + 滑动窗口

练习目标：
1) 熟练处理“区间动态扩缩”
2) 熟练维护窗口内状态（计数、和、去重）
3) 熟练在有序数组中使用对撞指针
"""

from typing import List, Tuple

from ._utils import run_cases


def longest_unique_segment(text: str) -> int:
    """
    TODO:
    返回 text 中不含重复字符的最长连续片段长度。
    """
    raise NotImplementedError("实现 longest_unique_segment")


def min_len_with_sum_at_least(nums: List[int], target: int) -> int:
    """
    TODO:
    返回和 >= target 的最短连续子数组长度，不存在返回 0。
    """
    raise NotImplementedError("实现 min_len_with_sum_at_least")


def pair_sum_in_sorted(nums: List[int], target: int) -> Tuple[int, int]:
    """
    TODO:
    nums 已升序，返回任意一组下标 (i, j)，使 nums[i] + nums[j] == target。
    若不存在，返回 (-1, -1)。
    """
    raise NotImplementedError("实现 pair_sum_in_sorted")


def partition_by_pivot(nums: List[int], pivot: int) -> List[int]:
    """
    TODO:
    原地重排，使得：
    - 小于 pivot 的元素在前
    - 等于 pivot 的元素在中
    - 大于 pivot 的元素在后
    返回重排后的数组。
    """
    raise NotImplementedError("实现 partition_by_pivot")


def run_checks() -> None:
    run_cases(
        "TODO 练习",
        [
            ("longest_unique_segment", lambda: longest_unique_segment("abcaefbg")),
            (
                "min_len_with_sum_at_least",
                lambda: min_len_with_sum_at_least([2, 3, 1, 2, 4, 3], 7),
            ),
            ("pair_sum_in_sorted", lambda: pair_sum_in_sorted([1, 2, 4, 6, 9], 10)),
            (
                "partition_by_pivot",
                lambda: partition_by_pivot([5, 1, 8, 5, 2, 5, 9], 5),
            ),
        ],
    )
