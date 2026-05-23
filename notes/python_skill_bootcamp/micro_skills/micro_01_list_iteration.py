"""
微技能 01：List 正着/倒着/双指针

训练点：
1) 正序遍历（for i in range(n)）
2) 倒序遍历（for i in range(n-1, -1, -1)）
3) 双指针（left/right）
"""

from typing import List

from ._utils import run_cases


def sum_at_even_index(nums: List[int]) -> int:
    """
    已实现：
    正序遍历，累加偶数下标元素。
    """
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
    return total


def reverse_copy(nums: List[int]) -> List[int]:
    """
    TODO:
    用“倒序遍历”手写反转副本，不能直接用 nums[::-1]。
    """
    r = []
    for i in range(len(nums)-1, -1, -1):
        r.append(nums[i])
    return r


def reverse_in_place(nums: List[int]) -> List[int]:
    """
    TODO:
    用双指针原地反转列表，并返回 nums。
    """
    i, j = 0, len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums



def merge_two_sorted_lists(a: List[int], b: List[int]) -> List[int]:
    """
    TODO:
    双指针合并两个有序列表。
    """
    i, j = 0,0
    res = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            ("sum_at_even_index", lambda: sum_at_even_index([10, 20, 30, 40, 50])),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            ("reverse_copy", lambda: reverse_copy([1, 2, 3, 4])),
            ("reverse_in_place", lambda: reverse_in_place([1, 2, 3, 4, 5])),
            ("merge_two_sorted_lists", lambda: merge_two_sorted_lists([1, 3, 5], [2, 4, 6])),
        ],
    )
