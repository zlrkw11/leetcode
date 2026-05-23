"""
技能组合 06：动态规划 + 状态转移

练习目标：
1) 定义状态（dp[i] 或 dp[i][j]）
2) 写出转移方程
3) 处理初始化与边界
"""

from typing import List, Set

from ._utils import run_cases


def max_non_adjacent_sum(nums: List[int]) -> int:
    """
    TODO:
    不能选相邻元素，求可选元素最大和。
    提示：滚动变量优化空间。
    """
    raise NotImplementedError("实现 max_non_adjacent_sum")


def min_path_sum(grid: List[List[int]]) -> int:
    """
    TODO:
    只能向右或向下，求左上到右下的最小路径和。
    """
    raise NotImplementedError("实现 min_path_sum")


def word_break_possible(text: str, dictionary: Set[str]) -> bool:
    """
    TODO:
    text 是否能被 dictionary 中的词完全拼接。
    提示：dp[i] 表示前 i 个字符是否可拆分。
    """
    raise NotImplementedError("实现 word_break_possible")


def longest_increasing_subsequence_len(nums: List[int]) -> int:
    """
    已实现版本（O(n^2)）：
    - dp[i] 表示以 nums[i] 结尾的 LIS 长度
    """
    if not nums:
        return 0

    dp = [1] * len(nums)
    best = 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        best = max(best, dp[i])

    return best


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            (
                "longest_increasing_subsequence_len",
                lambda: longest_increasing_subsequence_len([10, 9, 2, 5, 3, 7, 101, 18]),
            ),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            ("max_non_adjacent_sum", lambda: max_non_adjacent_sum([2, 7, 9, 3, 1])),
            (
                "min_path_sum",
                lambda: min_path_sum(
                    [
                        [1, 3, 1],
                        [1, 5, 1],
                        [4, 2, 1],
                    ]
                ),
            ),
            (
                "word_break_possible",
                lambda: word_break_possible("applepenapple", {"apple", "pen"}),
            ),
        ],
    )


if __name__ == "__main__":
    run_checks()
