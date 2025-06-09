from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    completed: bool = False

todos = []
todo_id_counter = 1

# Create a new todo item
@app.post("/todos")
def create_todo(todo: Todo):
    global todo_id_counter
    todo_with_id={
        "id": todo_id_counter,
        "title": todo.title,
        "completed": todo.completed
    }
    todos.append(todo_with_id)
    todo_id_counter += 1
    return {"message": "Task added successfully!",
             "task": todo_with_id}

@app.get("/todos")
def get_all_todos():
    return {"tasks": todos}

