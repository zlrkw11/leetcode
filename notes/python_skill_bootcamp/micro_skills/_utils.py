from typing import Any, Callable, Iterable, Tuple

Case = Tuple[str, Callable[[], Any]]


def run_cases(title: str, cases: Iterable[Case]) -> None:
    print(f"\n[{title}]")
    for idx, (name, fn) in enumerate(cases, start=1):
        try:
            result = fn()
            print(f"{idx}. {name}: {result}")
        except NotImplementedError as error:
            print(f"{idx}. {name}: 未完成 -> {error}")
        except Exception as error:  # noqa: BLE001
            print(f"{idx}. {name}: 运行异常 -> {error}")
