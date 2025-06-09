from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    completed: bool = False

todos = []

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Task added successfully!", "task": todo}

@app.get("/todos")
def get_all_todos():
    return {"tasks": todos}

