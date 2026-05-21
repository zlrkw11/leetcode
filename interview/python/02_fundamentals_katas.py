"""
Python fundamentals 练习题（手写版）
说明：
- 每个函数包含 TODO，请你自己实现。
- 运行后会提示哪些题目还未完成。
"""


def two_sum(nums, target):
    """
    TODO:
    给定数组 nums 和目标值 target，返回两个下标。
    假设每种输入只会对应一个答案，且不能重复使用同一元素。
    示例: nums=[2,7,11,15], target=9 => [0,1]
    """
    d = {}
    for i, n in enumerate(nums):
        x = target - n
        if x in d:
            return d[x, i]
        d[n] = i 
    return []

def is_palindrome(s):
    """
    TODO:
    只考虑字母和数字，忽略大小写，判断是否回文。
    示例: "A man, a plan, a canal: Panama" => True
    """
    raise NotImplementedError("TODO: 实现 is_palindrome")


def top_k_frequent(nums, k):
    """
    TODO:
    返回出现频率最高的 k 个元素。
    示例: nums=[1,1,1,2,2,3], k=2 => [1,2]
    """
    raise NotImplementedError("TODO: 实现 top_k_frequent")


def merge_intervals(intervals):
    """
    TODO:
    合并重叠区间。
    示例: [[1,3],[2,6],[8,10],[15,18]] => [[1,6],[8,10],[15,18]]
    """
    raise NotImplementedError("TODO: 实现 merge_intervals")


def first_unique_char(s):
    """
    TODO:
    返回字符串中第一个不重复字符的下标，不存在返回 -1。
    示例: "leetcode" => 0, "aabb" => -1
    """
    raise NotImplementedError("TODO: 实现 first_unique_char")


def run_checks():
    print("== Python Fundamentals Katas ==")
    print("把 TODO 实现后再运行，检查输出是否合理。\n")

    checks = [
        lambda: two_sum([2, 7, 11, 15], 9),
        lambda: is_palindrome("A man, a plan, a canal: Panama"),
        lambda: top_k_frequent([1, 1, 1, 2, 2, 3], 2),
        lambda: merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
        lambda: first_unique_char("leetcode"),
    ]

    for i, fn in enumerate(checks, start=1):
        try:
            result = fn()
            print(f"第 {i} 题结果: {result}")
        except NotImplementedError as error:
            print(f"第 {i} 题未完成: {error}")

    print("\n面试建议：")
    print("1) 每题先说复杂度，再写代码。")
    print("2) 先保证正确，再优化。")
    print("3) 至少覆盖空输入、重复值、极端边界。")


if __name__ == "__main__":
    run_checks()
