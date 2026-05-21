"use strict";

/**
 * 主题：var / let / const 区别
 * 重点：作用域、提升、暂时性死区、重复声明、const 的“引用不可变”
 */

function demoScope() {
  console.log("== 1) 作用域 ==");

  if (true) {
    var varInBlock = "var 在块里声明";
    let letInBlock = "let 在块里声明";
    const constInBlock = "const 在块里声明";

    console.log("块内部可访问:", varInBlock, letInBlock, constInBlock);
  }

  // var 是函数作用域，不是块作用域，所以这里还能访问
  console.log("块外访问 var:", varInBlock);

  // let / const 是块作用域，块外访问会报错
  // console.log(letInBlock);   // ReferenceError
  // console.log(constInBlock); // ReferenceError
}

function demoHoistingAndTDZ() {
  console.log("\n== 2) 提升与暂时性死区(TDZ) ==");

  // var 声明会被提升为 undefined
  console.log("var 提升结果:", beforeVar); // undefined
  var beforeVar = "现在才赋值";

  try {
    // let 声明前访问会触发 TDZ
    console.log(beforeLet);
  } catch (error) {
    console.log("let 在声明前访问报错:", error.message);
  }
  let beforeLet = "let 已声明";

  try {
    console.log(beforeConst);
  } catch (error) {
    console.log("const 在声明前访问报错:", error.message);
  }
  const beforeConst = "const 已声明";
}

function demoRedeclare() {
  console.log("\n== 3) 重复声明 ==");

  var a = 1;
  var a = 2; // var 允许重复声明（容易引发覆盖 bug）
  console.log("var 可重复声明:", a);

  let b = 1;
  // let b = 2; // SyntaxError: Identifier 'b' has already been declared
  console.log("let 不允许同一作用域重复声明:", b);

  const c = 1;
  // const c = 2; // SyntaxError
  console.log("const 不允许同一作用域重复声明:", c);
}

function demoConstMutation() {
  console.log("\n== 4) const 的关键点 ==");

  // const 保证“变量绑定”不可重新赋值
  const user = { name: "Alice", level: 1 };

  // 可以修改对象内部属性
  user.level = 2;
  console.log("const 对象属性可变:", user);

  // 不能把 user 重新指向另一个对象
  // user = { name: "Bob" }; // TypeError
}

function interviewSummary() {
  console.log("\n== 5) 面试回答模板 ==");
  console.log("1) 默认用 const，表达“不需要重新赋值”。");
  console.log("2) 需要重新赋值时用 let。");
  console.log("3) 避免 var，因为函数作用域+提升容易造成隐藏 bug。");
  console.log("4) 明确说明 TDZ：let/const 在声明前不可访问。");
}

/**
 * TODO 练习：
 * 1. 把你旧代码里的 var 全改成 let/const，并解释每一处选择。
 * 2. 写一个 for 循环 + setTimeout，比较 var 与 let 的输出差异。
 * 3. 用一句话解释：为什么 const 对象还能改属性？
 */

demoScope();
demoHoistingAndTDZ();
demoRedeclare();
demoConstMutation();
interviewSummary();
