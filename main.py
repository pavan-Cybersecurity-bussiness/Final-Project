from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from file_handler import load_tasks, save_tasks
import json
import os
from models import TaskCreate ,Task, TaskUpdate

app =FastAPI()
#root
@app.get("/")
def root():
    return {"message": "Task API is running."}

"""
#number 1 get all task
@app.get("/tasks")
def get_all_tasks():
    tasks = load_tasks()
    return tasks
"""
#number 1& 7 get all task and filter based on parameter
@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()

    if completed is None:
        return tasks

    filtered_tasks = []

    for task in tasks:
        if task["completed"] == completed:
            filtered_tasks.append(task)

    return filtered_tasks
@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks = load_tasks()
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    new_task = {
       "id": new_id,
        # current approach is better than "id": len(tasks) + 1, this avoids duplication of task ids
        "title": task.title,
        "completed": False,
        "description": task.description
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

# number 9 placed here to avoid route conflict since dynamic route is used
@app.get("/tasks/stats")
def get_task_stats():
    tasks = load_tasks()

    total = len(tasks)

    completed_count = 0
    for task in tasks:
        if task["completed"] is True:
            completed_count += 1

    pending_count = total - completed_count

    if total == 0:
        completion_percentage = 0
    else:
        completion_percentage = round((completed_count / total) * 100,2)

    return {
        "total_tasks": total,
        "completed_tasks": completed_count,
        "pending_tasks": pending_count,
        "completion_percentage": completion_percentage
    }
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    tasks = load_tasks()

    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = updated_task.title
            existing_task["description"] = updated_task.description
            existing_task["completed"] = updated_task.completed
            save_tasks(tasks)
            return existing_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks")
def delete_all_tasks():
    tasks = load_tasks()
    count = len(tasks)
    save_tasks([])
    return {"deleted_count": count ,"message" : "all tasks deleted"}
