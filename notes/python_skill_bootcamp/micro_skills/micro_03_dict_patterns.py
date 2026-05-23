"""
微技能 03：Dict 常见模式

训练点：
1) 频次统计
2) 分组聚合
3) Key 不存在时的默认处理
"""

from typing import Dict, List, Tuple

from ._utils import run_cases


def count_frequency(nums: List[int]) -> Dict[int, int]:
    """
    TODO:
    统计每个数字出现次数。
    """
    raise NotImplementedError("实现 count_frequency")


def group_names_by_initial(names: List[str]) -> Dict[str, List[str]]:
    """
    TODO:
    按首字母分组，返回 {initial: [name1, name2, ...]}。
    规则：首字母统一小写；组内保持输入顺序。
    """
    raise NotImplementedError("实现 group_names_by_initial")


def accumulate_scores(records: List[Tuple[str, int]]) -> Dict[str, int]:
    """
    已实现：
    多条 (name, score) 记录，按 name 累加总分。
    """
    total: Dict[str, int] = {}
    for name, score in records:
        total[name] = total.get(name, 0) + score
    return total


def first_unique_char_index(text: str) -> int:
    """
    TODO:
    返回首个只出现一次字符的下标，不存在返回 -1。
    """
    raise NotImplementedError("实现 first_unique_char_index")


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            (
                "accumulate_scores",
                lambda: accumulate_scores([("a", 10), ("b", 8), ("a", 7)]),
            ),
        ],
    )
    run_cases(
        "TODO 练习",
        [
            ("count_frequency", lambda: count_frequency([3, 1, 3, 2, 1, 3])),
            ("group_names_by_initial", lambda: group_names_by_initial(["Alice", "adam", "Bob", "bella"])),
            ("first_unique_char_index", lambda: first_unique_char_index("aabbcddee")),
        ],
    )
