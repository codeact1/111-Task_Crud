from flask import Flask, request
from app.database import task

app = Flask(__name__)


@app.get("/tasks")
def get_all_tasks():
    out = {} 
    response = task.scan()
    out["tasks"] = response
    return out


@app.post("/tasks")
def create_task():
    out = {"status": "ok"}
    task_data = request.json
    task.insert(task_data)
    return out, 201


@app.put("/tasks")
def update_task():
    out = {"status": "ok"}
    task_data = request.json
    task.update(task_data)
    return out, 201

@app.delete("/tasks")
def delete_task():
    out = {"status": "ok"}
    task_data = request.json
    task.delete(task_data)
    return out, 201






