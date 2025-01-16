from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WarehouseDB(BaseModel):
    id: int
    location: str

class ItemDB(BaseModel):
    id: int
    name: str

WAREHOUSE_DB = [
     WarehouseDB(id= 1, location= "Кукуево 13"),
     WarehouseDB(id= 2, location= "Кузнецово 3А"),
     WarehouseDB(id= 3, location= "Эзотерическая 42"),
]

ITEM_DB = [
    ItemDB(id= 1, name= "Диван Скуф"),
    ItemDB(id= 2, name= "Стол Стоялов"),
    ItemDB(id= 3, name= "Кресло Хакерман"),
]

@app.get("/")
def root():
    return {"message": "Работа FastAPI"}


@app.get("/warehouse/{warehouse_id}")
def warehouse_number(warehouse_id: int):
    for warehouse in WAREHOUSE_DB:
        if warehouse.id == warehouse_id:
            return warehouse
        
@app.get("/warehouse/")
def warehouses():
    return WAREHOUSE_DB

@app.get("/item/{item_id}")
def item_number (item_id: int):
    for item in ITEM_DB:
        if item.id == item_id:
            return item

@app.get("/item/")
def items():
    return ITEM_DB
