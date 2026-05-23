from typing import Any, Callable, Iterable, List, Tuple

Case = Tuple[str, Callable[[], Any]]


def run_cases(title: str, cases: Iterable[Case]) -> None:
    """
    统一执行样例：
    - TODO 未实现时给出友好提示
    - 已实现时输出结果，便于快速回归
    """
    print(f"\n[{title}]")
    for idx, (name, fn) in enumerate(cases, start=1):
        try:
            result = fn()
            print(f"{idx}. {name}: {result}")
        except NotImplementedError as error:
            print(f"{idx}. {name}: 未完成 -> {error}")
        except Exception as error:  # noqa: BLE001
            print(f"{idx}. {name}: 运行异常 -> {error}")


def assert_equal(actual: Any, expected: Any, label: str = "") -> str:
    """
    简化断言展示：
    - 返回 OK / FAIL 字符串
    - 让你在不依赖 pytest 的情况下快速看结果
    """
    if actual == expected:
        return f"OK {label}".strip()
    return f"FAIL {label} | actual={actual} expected={expected}".strip()


def pretty_list(values: List[Any]) -> str:
    """统一列表输出格式，便于阅读。"""
    return "[" + ", ".join(str(v) for v in values) + "]"
