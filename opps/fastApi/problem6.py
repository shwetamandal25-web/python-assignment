from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": True},
    {"id": 2, "title": "Build a GET endpoint", "done": False},
    {"id": 3, "title": "Build a POST endpoint", "done": False},
]


class TaskCreate(BaseModel):
    title: str
    done: bool


# ONE HELPER
def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# GET ONE TASK
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return find_task(task_id)


# PUT / UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):

    existing_task = find_task(task_id)

    existing_task["title"] = task.title
    existing_task["done"] = task.done

    return existing_task


# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    existing_task = find_task(task_id)

    tasks.remove(existing_task)

    return {"message": "Task deleted successfully"}