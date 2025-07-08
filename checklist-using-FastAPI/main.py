from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from typing import List
# from authHelper import *

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

todo_list = []

def authorizeAPI(request: Request):
    api_key = request.headers.get("X-API-Key")
    expected_key = "mytoken"  # You can also load this from env or config

    if api_key != expected_key:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")

    return api_key  # Optional return if you want to use it later

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Checklist"}

@app.get("/todos", dependencies=[Depends(authorizeAPI)])
def get_todo_list():
    return todo_list

@app.post("/todos", response_model=List[TodoItem], dependencies=[Depends(authorizeAPI)] )
def create_item(item: TodoItem):
    todo_list.append(item)
    return item

@app.post("/todos/{item_id}", response_model=List[TodoItem], dependencies=[Depends(authorizeAPI)])
def get_todo_item(item_id: int):
    for item in todo_list:
        if item_id == item.id:
            return item
    raise HTTPException(status_code=404, detail="Item not found.")

@app.post("/delete/{item_id}", response_model=List[TodoItem], dependencies=[Depends(authorizeAPI)])
def delete_todo_item(item_id: int):
    global todo_list
    todo_list = [item for item in todo_list if item.id != item_id]
    return {"message": f"Item with id {item_id} deleted"}