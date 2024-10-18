from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# GET request at the root
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# GET request for items
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Pydantic model for item data
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None

# PUT request to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
