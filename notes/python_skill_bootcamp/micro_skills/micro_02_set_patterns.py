"""
微技能 02：Set 常见模式

训练点：
1) 去重
2) 交集/差集
3) visited 集合防重复访问
"""

from typing import List

from ._utils import run_cases


def unique_count(nums: List[int]) -> int:
    """
    已实现：
    返回去重后元素个数。
    """
    return len(set(nums))


def intersection_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    TODO:
    返回 a 和 b 的交集（去重），并按升序输出。
    """
    sa = set(a)
    sb = set(b)

    c = sa.intersection(sb)
    return sorted(c)
    


def first_repeated_value(nums: List[int]) -> int:
    """
    TODO:
    返回第一个重复出现的值（按扫描顺序），若无重复返回 -1。
    提示：用 visited set。
    """
    visited = set()
    for n in nums:
        if n in visited:
            return n 
        visited.add(n)
    return -1


def longest_non_repeat_prefix(text: str) -> int:
    """
    TODO:
    从左往右扫描，返回“前缀中没有重复字符”的最大长度。
    示例：'abca' -> 3（'abc'）
    """
    rec = 0
    curr = set()
    for t in text:

        if t in curr:
            if len(curr) > rec:
                rec = len(curr)
            return rec 
        

        else:
            curr.add(t)
            
    return max(rec, len(curr))  



def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            ("unique_count", lambda: unique_count([1, 1, 2, 3, 3, 3])),
        ],
    )
    run_cases(
        "TODO 练习",
        [
            ("intersection_sorted", lambda: intersection_sorted([4, 1, 2, 2], [2, 4, 4, 6])),
            ("first_repeated_value", lambda: first_repeated_value([5, 1, 3, 1, 4])),
            ("longest_non_repeat_prefix", lambda: longest_non_repeat_prefix("abcaef")),
        ],
    )
