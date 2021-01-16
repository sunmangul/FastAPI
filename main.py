from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):  #객체의 타입을 정의할 떄는 BaseModel에서 상속 받아서 사용
    price: float
    is_offer: Optional[bool] = None

@app.get('/') # / get 요청이 오면 응답값으로 "Hello world" 반환
def read_root():
    return "Hello world"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/add")
def add_item(item: Item):
    print(item)
    return {"success": True}