"""
技能组合 04：栈 + 队列 + 堆

练习目标：
1) 熟练 LIFO/FIFO 思维
2) 熟练单调栈处理“下一个更大/更小”
3) 熟练最小堆维护 Top-K
"""

import heapq
from collections import deque
from typing import List

from ._utils import run_cases


def is_brackets_valid(text: str) -> bool:
    """
    TODO:
    只包含 ()[]{}，判断括号序列是否合法。
    """
    raise NotImplementedError("实现 is_brackets_valid")


def next_greater_distance(nums: List[int]) -> List[int]:
    """
    TODO:
    对每个位置 i，返回右侧第一个更大元素到 i 的距离；
    若不存在，返回 0。
    提示：单调递减栈存下标。
    """
    raise NotImplementedError("实现 next_greater_distance")


def top_k_largest(nums: List[int], k: int) -> List[int]:
    """
    TODO:
    返回最大的 k 个数（降序输出）。
    提示：维护大小为 k 的最小堆。
    """
    raise NotImplementedError("实现 top_k_largest")


def moving_average(stream: List[int], window_size: int) -> List[float]:
    """
    用队列实现滑动平均（已实现）：
    - 每次新增一个元素
    - 超过窗口大小就弹出最旧元素
    """
    if window_size <= 0:
        return []

    q: deque[int] = deque()
    running_sum = 0
    result: List[float] = []

    for value in stream:
        q.append(value)
        running_sum += value

        if len(q) > window_size:
            running_sum -= q.popleft()

        result.append(running_sum / len(q))

    return result


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            ("moving_average", lambda: moving_average([10, 20, 30, 40], 2)),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            ("is_brackets_valid", lambda: is_brackets_valid("({[]})[]")),
            ("next_greater_distance", lambda: next_greater_distance([2, 1, 2, 4, 3])),
            ("top_k_largest", lambda: top_k_largest([3, 1, 5, 12, 2, 11], 3)),
        ],
    )


if __name__ == "__main__":
    # 支持单文件直跑，便于你专注练某个模块
    run_checks()
