"""
微技能 04：字符串处理模式

训练点：
1) 双指针判断回文
2) 连续字符压缩（run-length encoding）
3) 子串窗口统计
"""

from typing import Dict

from ._utils import run_cases


def normalize_letters_digits(text: str) -> str:
    """
    已实现：
    只保留字母数字并转小写。
    """
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch.lower())
    return "".join(out)


def is_palindrome_text(text: str) -> bool:
    """
    TODO:
    忽略非字母数字和大小写，判断是否回文。
    """
    raise NotImplementedError("实现 is_palindrome_text")


def run_length_encode(text: str) -> str:
    """
    TODO:
    连续字符压缩：'aaabbc' -> 'a3b2c1'
    """
    raise NotImplementedError("实现 run_length_encode")


def min_window_cover_length(text: str, required: str) -> int:
    """
    TODO:
    返回最短子串长度，使其覆盖 required 的所有字符（含重复）。
    不存在则返回 0。
    """
    raise NotImplementedError("实现 min_window_cover_length")


def run_checks() -> None:
    run_cases(
        "Warmup（已实现）",
        [
            ("normalize_letters_digits", lambda: normalize_letters_digits("A man, a plan! 123")),
        ],
    )
    run_cases(
        "TODO 练习",
        [
            ("is_palindrome_text", lambda: is_palindrome_text("A man, a plan, a canal: Panama")),
            ("run_length_encode", lambda: run_length_encode("aaabbc")),
            ("min_window_cover_length", lambda: min_window_cover_length("ADOBECODEBANC", "ABC")),
        ],
    )
