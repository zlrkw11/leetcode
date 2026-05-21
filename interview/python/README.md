# Python 面试基础练习

## 文件说明

- `01_generators.py`：generator 核心概念 + 可运行示例。
- `02_fundamentals_katas.py`：Python 基础手写题（TODO）。
- `03_basic_api_fastapi.py`：基础 API 构建模板（FastAPI）。
- `requirements.txt`：API 示例依赖。

## 运行方式

```bash
python3 interview/python/01_generators.py
python3 interview/python/02_fundamentals_katas.py
```

API 示例运行：

```bash
pip install -r interview/python/requirements.txt
uvicorn interview.python.03_basic_api_fastapi:app --reload
```

访问：

- `GET http://127.0.0.1:8000/health`
- `GET http://127.0.0.1:8000/items`
- `POST http://127.0.0.1:8000/items`

## 练习建议

1. generator 的题目，先画出每次 `yield` 暂停的位置。
2. 每个 TODO 先写最朴素版本，再优化时间复杂度。
3. API 模板先跑通，再自己加一个新路由（例如删除 item）。
