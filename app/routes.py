from flask import (
    Flask,
    request
)

from app.database import task

app = Flask(__name__)
#Rest: an architectural design pattern for building connected ssytems.
#Name endpoints after plural known ex: ("Orders/Tasks/Lists")
#PK = Primary Key
@app.get("/tasks")
def get_all_tasks():
    tasks = task.scan()
    out = {
        "tasks": tasks,
        "ok":True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    out = {
        "tasks": single_task,
        "ok":True
    }
    return out

@app.post("/tasks")
def create_tasks():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task_by_id(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "",204

@app.delete("/tasks/<int:pk>/")
def delete_task_by_id(pk):
    task.delete_by_id(pk)
    return "",204