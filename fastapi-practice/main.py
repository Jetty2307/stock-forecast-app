from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"} 

@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"items": list(range(skip, skip + limit))}

from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "message": "Item created successfully!"}

@app.get("/products/{product_id}")
def read_product(product_id: int):
    if product_id > 100:
        return {"error": "Product not found"}
    return {"product_id": product_id, "details": "This is a sample product"}

from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": "John Doe"}

class Product(BaseModel):
    id: int
    name: str
    price: float

@app.get("/product_id/{product_id}", response_model=Product)
def get_product(product_id: int):
    return {"id": product_id, "name": "Sample Product", "price": 99.99}
