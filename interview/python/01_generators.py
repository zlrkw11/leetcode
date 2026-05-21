"""
主题：Python generators
重点：yield、惰性求值、next/send/yield from
"""


def count_up_to(n):
    """从 1 生成到 n（惰性生成，不一次性占用大内存）"""
    current = 1
    while current <= n:
        yield current
        current += 1


def fibonacci(limit):
    """生成不超过 limit 的斐波那契数"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def echo():
    """
    演示 send()：
    - 第一次必须 next(gen) 或 gen.send(None) 启动生成器
    - 之后可以 send(value) 传值回生成器内部
    """
    received = "init"
    while True:
        # yield 把值给外部，同时等待外部 send 新值回来
        received = yield f"收到: {received}"


def flatten(list_of_lists):
    """演示 yield from：把子迭代器的值直接透传出去"""
    for sub in list_of_lists:
        yield from sub


def main():
    print("== 1) count_up_to ==")
    for x in count_up_to(5):
        print(x, end=" ")
    print("\n")

    print("== 2) fibonacci ==")
    print(list(fibonacci(30)))
    print()

    print("== 3) send() ==")
    g = echo()
    print(next(g))          # 启动生成器
    print(g.send("hello"))  # 传值
    print(g.send("world"))  # 再传值
    print()

    print("== 4) yield from ==")
    nested = [[1, 2], [3], [4, 5]]
    print(list(flatten(nested)))
    print()

    print("== 5) 面试回答模板 ==")
    print("1) generator 是实现了迭代器协议的函数，核心是 yield。")
    print("2) 优势是惰性计算、省内存，适合流式数据。")
    print("3) send() 可以把值发回生成器，协程早期模型常见。")
    print("4) yield from 用于委托子生成器，减少样板代码。")

    print("\n== TODO 练习 ==")
    print("1) 写一个 generator，只生成偶数。")
    print("2) 写一个读取大文件的 generator，每次 yield 一行。")
    print("3) 写一个 sliding window generator，给定 window_size 输出窗口切片。")


if __name__ == "__main__":
    main()
