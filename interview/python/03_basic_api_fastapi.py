"""
基础 Python API 构建模板（FastAPI）

运行：
1) pip install -r interview/python/requirements.txt
2) uvicorn interview.python.03_basic_api_fastapi:app --reload
"""

from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 创建应用实例
app = FastAPI(title="Interview Practice API", version="0.1.0")


class ItemCreate(BaseModel):
    """创建请求体：用户提交的数据"""

    name: str = Field(min_length=1, max_length=50, description="商品名")
    price: float = Field(gt=0, description="价格，必须 > 0")
    tags: List[str] = Field(default_factory=list, description="标签列表")


class Item(ItemCreate):
    """响应体：在创建请求体基础上增加 id"""

    id: int


# 用内存字典模拟数据库
ITEMS: Dict[int, Item] = {}
NEXT_ID = 1


@app.get("/health")
def health_check():
    """健康检查接口"""
    return {"status": "ok"}


@app.get("/items", response_model=List[Item])
def list_items():
    """查询全部 items"""
    return list(ITEMS.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """按 ID 查询单个 item"""
    item = ITEMS.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    """创建 item"""
    global NEXT_ID
    item = Item(id=NEXT_ID, **payload.model_dump())
    ITEMS[NEXT_ID] = item
    NEXT_ID += 1
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate):
    """更新 item（全量更新）"""
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="item not found")

    updated = Item(id=item_id, **payload.model_dump())
    ITEMS[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """删除 item"""
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="item not found")
    del ITEMS[item_id]


"""
TODO 练习：
1) 增加分页参数：/items?page=1&page_size=10
2) 增加模糊搜索：按 name 查询
3) 增加异常处理中间件，统一错误返回格式
4) 把内存存储替换成 SQLite（如 SQLModel / SQLAlchemy）
"""
