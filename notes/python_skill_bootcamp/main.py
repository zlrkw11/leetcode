#!/usr/bin/env python3
"""
统一运行入口：
- 列出可练习模块
- 单独运行某个模块
- 运行全部模块
"""

import argparse
import os
import sys
from typing import Callable, Dict

# 确保可以导入同目录下的 skills 包
ROOT_DIR = os.path.dirname(__file__)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from skills import (  # noqa: E402
    skill_01_hash_and_sort,
    skill_02_window_and_two_pointers,
    skill_03_prefix_diff_and_binary_search,
    skill_04_stack_queue_heap,
    skill_05_graph_and_backtracking,
    skill_06_dp_and_state_transition,
)

MODULES: Dict[str, Callable[[], None]] = {
    "skill_01_hash_and_sort": skill_01_hash_and_sort.run_checks,
    "skill_02_window_and_two_pointers": skill_02_window_and_two_pointers.run_checks,
    "skill_03_prefix_diff_and_binary_search": skill_03_prefix_diff_and_binary_search.run_checks,
    "skill_04_stack_queue_heap": skill_04_stack_queue_heap.run_checks,
    "skill_05_graph_and_backtracking": skill_05_graph_and_backtracking.run_checks,
    "skill_06_dp_and_state_transition": skill_06_dp_and_state_transition.run_checks,
}


def print_modules() -> None:
    print("可用模块：")
    for name in MODULES:
        print(f"- {name}")


def run_one(module_name: str) -> None:
    fn = MODULES.get(module_name)
    if fn is None:
        print(f"模块不存在: {module_name}")
        print_modules()
        return
    print(f"\n===== 运行 {module_name} =====")
    fn()


def run_all() -> None:
    for module_name in MODULES:
        run_one(module_name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Python 技巧组合训练入口")
    parser.add_argument("--list", action="store_true", help="列出所有模块")
    parser.add_argument("--module", type=str, help="只运行某个模块")
    parser.add_argument("--all", action="store_true", help="运行全部模块")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.list:
        print_modules()
        return

    if args.module:
        run_one(args.module)
        return

    # 默认行为：跑全部
    if args.all or (not args.list and not args.module):
        run_all()


if __name__ == "__main__":
    main()
