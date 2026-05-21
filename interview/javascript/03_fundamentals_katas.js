"use strict";

/**
 * JavaScript fundamentals 练习题（手写版）
 * 说明：
 * - 每题先自己写，再运行本文件看结果。
 * - 当前函数故意留空（TODO），用于练习。
 */

function reverseWords(sentence) {
  // TODO: 反转句子中的单词顺序（不是反转单词字符）
  // 示例: "i love js" => "js love i"
  throw new Error("TODO: 实现 reverseWords");
}

function countCharFrequency(text) {
  // TODO: 统计每个字符出现次数，返回对象
  // 示例: "aab" => { a: 2, b: 1 }
  throw new Error("TODO: 实现 countCharFrequency");
}

function mergeUnique(nums1, nums2) {
  // TODO: 合并两个数组并去重，返回升序数组
  // 示例: [3,1,2], [2,4] => [1,2,3,4]
  throw new Error("TODO: 实现 mergeUnique");
}

function groupByAge(users) {
  // TODO: 按 age 分组
  // 输入: [{name:'a', age:18}, {name:'b', age:20}, {name:'c', age:18}]
  // 输出: { "18": [...], "20": [...] }
  throw new Error("TODO: 实现 groupByAge");
}

function once(fn) {
  // TODO: 实现 once，高阶函数只允许 fn 执行一次
  // 后续调用直接返回第一次结果
  throw new Error("TODO: 实现 once");
}

function runChecks() {
  console.log("== JS Fundamentals Katas ==");
  console.log("把每个 TODO 实现后重新运行本文件。\n");

  const checks = [
    () => reverseWords("i love js"),
    () => countCharFrequency("aabcc"),
    () => mergeUnique([3, 1, 2], [2, 4]),
    () =>
      groupByAge([
        { name: "a", age: 18 },
        { name: "b", age: 20 },
        { name: "c", age: 18 },
      ]),
    () => {
      const add = (a, b) => a + b;
      const addOnce = once(add);
      return [addOnce(1, 2), addOnce(3, 4), addOnce(10, 20)];
    },
  ];

  checks.forEach((fn, idx) => {
    try {
      const result = fn();
      console.log(`第 ${idx + 1} 题结果:`, result);
    } catch (error) {
      console.log(`第 ${idx + 1} 题未完成:`, error.message);
    }
  });
}

/**
 * 面试补充建议：
 * 1. 写题时先说时间复杂度和边界条件。
 * 2. 优先写可读性，再优化微小性能。
 * 3. 每题至少补 2 个边界测试：空输入、重复值、异常类型。
 */

runChecks();
