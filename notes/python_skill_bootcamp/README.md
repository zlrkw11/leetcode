# Python Skill Bootcamp（编程技巧组合练习）

这个目录不是刷具体题号，而是按“技能组合”训练你：

- 哈希 + 排序 + 统计
- 双指针 + 滑动窗口
- 前缀和 + 差分 + 二分
- 栈 + 堆 + 队列
- 图搜索 + 回溯
- 动态规划 + 状态转移

## 目录结构

```text
notes/python_skill_bootcamp/
  main.py
  micro_main.py
  skills/
    _utils.py
    skill_01_hash_and_sort.py
    skill_02_window_and_two_pointers.py
    skill_03_prefix_diff_and_binary_search.py
    skill_04_stack_queue_heap.py
    skill_05_graph_and_backtracking.py
    skill_06_dp_and_state_transition.py
  micro_skills/
    __init__.py
    _utils.py
    micro_01_list_iteration.py
    micro_02_set_patterns.py
    micro_03_dict_patterns.py
    micro_04_string_patterns.py
    micro_05_matrix_basics.py
    micro_06_matrix_prefix_and_neighbors.py
```

## 使用方式

先列出所有模块：

```bash
python3 notes/python_skill_bootcamp/main.py --list
```

只练某一个模块：

```bash
python3 notes/python_skill_bootcamp/main.py --module skill_02_window_and_two_pointers
```

一次跑全部模块：

```bash
python3 notes/python_skill_bootcamp/main.py --all
```

## 微技能练习（更细粒度）

列出微技能模块：

```bash
python3 notes/python_skill_bootcamp/micro_main.py --list
```

只练一个微技能：

```bash
python3 notes/python_skill_bootcamp/micro_main.py --module micro_01_list_iteration
```

跑全部微技能：

```bash
python3 notes/python_skill_bootcamp/micro_main.py --all
```

## 训练方法（建议）

1. 先读每个函数上面的中文注释，口述思路和复杂度。
2. 把 `TODO` 函数实现出来，再跑检查。
3. 每个函数至少补 3 组自测：空输入、边界输入、随机输入。
4. 最后做限时训练：每题 15-20 分钟，超时就看提示重写。

## 进阶建议

1. 每周重做一次同一模块，目标是越写越快、越稳。
2. 每次重做必须手写，不复制历史答案。
3. 把自己常错的边界条件记录到单独笔记。
