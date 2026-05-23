#!/usr/bin/env python3
"""
微技能训练入口：
- 面向 set / dict / list / string / matrix 的细粒度练习
"""

import argparse
import os
import sys
from typing import Callable, Dict

ROOT_DIR = os.path.dirname(__file__)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from micro_skills import (  # noqa: E402
    micro_01_list_iteration,
    micro_02_set_patterns,
    micro_03_dict_patterns,
    micro_04_string_patterns,
    micro_05_matrix_basics,
    micro_06_matrix_prefix_and_neighbors,
)

MODULES: Dict[str, Callable[[], None]] = {
    "micro_01_list_iteration": micro_01_list_iteration.run_checks,
    "micro_02_set_patterns": micro_02_set_patterns.run_checks,
    "micro_03_dict_patterns": micro_03_dict_patterns.run_checks,
    "micro_04_string_patterns": micro_04_string_patterns.run_checks,
    "micro_05_matrix_basics": micro_05_matrix_basics.run_checks,
    "micro_06_matrix_prefix_and_neighbors": micro_06_matrix_prefix_and_neighbors.run_checks,
}


def print_modules() -> None:
    print("可用微技能模块：")
    for name in MODULES:
        print(f"- {name}")


def run_module(name: str) -> None:
    fn = MODULES.get(name)
    if fn is None:
        print(f"模块不存在: {name}")
        print_modules()
        return
    print(f"\n===== 运行 {name} =====")
    fn()


def run_all() -> None:
    for name in MODULES:
        run_module(name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Python 微技能训练入口")
    parser.add_argument("--list", action="store_true", help="列出模块")
    parser.add_argument("--module", type=str, help="运行单个模块")
    parser.add_argument("--all", action="store_true", help="运行全部模块")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.list:
        print_modules()
        return

    if args.module:
        run_module(args.module)
        return

    # 默认跑全部
    if args.all or (not args.list and not args.module):
        run_all()


if __name__ == "__main__":
    main()
