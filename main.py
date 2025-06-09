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

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated_todo.title
            todo["completed"] = updated_todo.completed
            return {
                "message": "Task updated successfully!",
                "task": todo
            }
    return {"error": "Task not found!"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted = todos.pop(index)
            return {
                "message": "Task deleted successfully!",
                "task": deleted
            }
    return {"error": "Task not found!"}
