"use strict";

/**
 * 主题：Promise 与 async/await
 * 重点：状态流转、错误处理、串行与并发
 */

function fakeRequest(name, ms, shouldFail = false) {
  // 用 Promise 模拟异步请求
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (shouldFail) {
        reject(new Error(`${name} 失败`));
        return;
      }
      resolve(`${name} 成功 (耗时 ${ms}ms)`);
    }, ms);
  });
}

function demoPromiseChain() {
  console.log("== 1) Promise 链式调用 ==");
  return fakeRequest("step1", 300)
    .then((res1) => {
      console.log(res1);
      return fakeRequest("step2", 200);
    })
    .then((res2) => {
      console.log(res2);
      return "链式调用结束";
    })
    .catch((error) => {
      console.log("链式调用出错:", error.message);
      return "链式调用失败";
    })
    .finally(() => {
      console.log("Promise finally: 不管成功或失败都会执行");
    });
}

async function demoAsyncAwait() {
  console.log("\n== 2) async/await 写法 ==");
  try {
    const a = await fakeRequest("A", 200);
    console.log(a);

    const b = await fakeRequest("B", 200);
    console.log(b);

    // 这里故意制造错误，看 try/catch 是否生效
    await fakeRequest("C", 150, true);
    console.log("不会执行到这里");
  } catch (error) {
    console.log("async/await 捕获错误:", error.message);
  } finally {
    console.log("async/await finally: 清理动作放这里");
  }
}

async function demoConcurrency() {
  console.log("\n== 3) 并发执行 ==");

  // Promise.all: 有一个失败就整体失败
  try {
    const results = await Promise.all([
      fakeRequest("并发任务1", 300),
      fakeRequest("并发任务2", 500),
      fakeRequest("并发任务3", 100),
    ]);
    console.log("Promise.all 结果:", results);
  } catch (error) {
    console.log("Promise.all 失败:", error.message);
  }

  // Promise.allSettled: 不会短路，能拿到全部结果
  const settled = await Promise.allSettled([
    fakeRequest("allSettled任务1", 100),
    fakeRequest("allSettled任务2", 120, true),
    fakeRequest("allSettled任务3", 80),
  ]);
  console.log("Promise.allSettled 结果:", settled);
}

function interviewSummary() {
  console.log("\n== 4) 面试回答模板 ==");
  console.log("1) Promise 是异步结果的容器，状态：pending/fulfilled/rejected。");
  console.log("2) async 函数本质返回 Promise。");
  console.log("3) await 让异步代码看起来像同步，错误用 try/catch。");
  console.log("4) 并发优先用 Promise.all；需要看全部结果用 Promise.allSettled。");
}

/**
 * TODO 练习：
 * 1. 写一个 timeout(ms) 函数，返回一个 Promise。
 * 2. 用 Promise.race 做“请求超时控制”。
 * 3. 把三个独立请求从串行改成并发，比较耗时。
 */

(async () => {
  const chainResult = await demoPromiseChain();
  console.log("链式返回值:", chainResult);
  await demoAsyncAwait();
  await demoConcurrency();
  interviewSummary();
})();
