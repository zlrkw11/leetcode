"""
技能组合 01：哈希 + 排序 + 统计

练习目标：
1) 熟悉 dict / set 的 O(1) 查找优势
2) 熟悉按多关键字排序
3) 熟悉“先聚合再排序”的数据处理套路
"""

from typing import Dict, List, Tuple

from ._utils import assert_equal, run_cases


def merge_latest_records(rows: List[Tuple[str, int, int]]) -> Dict[str, int]:
    """
    给定 (user_id, score, ts) 列表。
    需求：按 user_id 保留最新 ts 对应的 score。
    返回：{user_id: latest_score}

    示例：
    [("u1", 10, 100), ("u1", 15, 120)] -> {"u1": 15}
    """
    latest: Dict[str, Tuple[int, int]] = {}
    for user_id, score, ts in rows:
        if user_id not in latest or ts > latest[user_id][0]:
            latest[user_id] = (ts, score)
    return {user_id: info[1] for user_id, info in latest.items()}


def top_k_words(text: str, stop_words: set, k: int) -> List[Tuple[str, int]]:
    """
    TODO:
    统计 text 中每个单词出现次数，过滤 stop_words，
    然后按以下规则返回前 k 名：
    1) 次数降序
    2) 单词字典序升序（用于打破并列）

    返回格式：[(word, count), ...]
    """
    raise NotImplementedError("实现 top_k_words")


def longest_consecutive_streak(nums: List[int]) -> int:
    """
    TODO:
    给定整数数组，返回最长连续整数序列长度。
    要求平均 O(n)。

    提示：用 set 做快速存在性判断，只从“序列起点”开始扩展。
    """
    raise NotImplementedError("实现 longest_consecutive_streak")


def group_and_rank(players: List[Tuple[str, str, int]]) -> List[Tuple[str, str, int]]:
    """
    TODO:
    输入 (team, player, score)，输出排序后的列表：
    1) team 升序
    2) 同 team 内 score 降序
    3) 同 score 内 player 升序
    """
    raise NotImplementedError("实现 group_and_rank")


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            (
                "merge_latest_records",
                lambda: assert_equal(
                    merge_latest_records(
                        [
                            ("u1", 10, 100),
                            ("u2", 7, 110),
                            ("u1", 15, 120),
                            ("u2", 9, 105),
                        ]
                    ),
                    {"u1": 15, "u2": 7},
                    "keep latest by ts",
                ),
            ),
        ],
    )

    run_cases(
        "TODO 练习",
        [
            (
                "top_k_words",
                lambda: top_k_words(
                    "go go rust python go rust sql python", {"sql"}, 2
                ),
            ),
            (
                "longest_consecutive_streak",
                lambda: longest_consecutive_streak([100, 4, 200, 1, 3, 2]),
            ),
            (
                "group_and_rank",
                lambda: group_and_rank(
                    [
                        ("A", "alice", 90),
                        ("A", "bob", 90),
                        ("B", "tom", 88),
                        ("A", "carol", 95),
                    ]
                ),
            ),
        ],
    )
