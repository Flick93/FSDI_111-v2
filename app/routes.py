from flask import (
    Flask,
    render_template,   #alias for requests context object
    request as req
)

import requests       #this is the standalone request python package

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/tasks")
def view_tasks():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks") #json turned into python dictionary
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/")
def single_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk) #means of formatting a string
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("tasks") 
        return render_template("detail.html", tasks=task_data)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.get("/tasks/new/")
def new_form():
    return render_template("new.html")

@app.post("/tasks/new/")
def create_form():
    task_data = req.json
    response = requests.post(BACKEND_URL, task_data)
    if response.status_code == 204:
        return render_template("success.html", message="Task Created")
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/edit/")
def edit_form(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task") 
        return render_template("edit.html", task=task_data)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.post("/tasks/<int:pk>/edit/")
def edit_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.put(url, json=req.json)
    if response.status_code == 204:
        return render_template("success.html", message="Task Edited")
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/delete/")
def delete_form(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task") 
        return render_template("delete.html", task=task_data)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )

@app.post("/tasks/<int:pk>/delete/")
def delete_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.put(url)
    if response.status_code == 204:
        return render_template("success.html", message="Task Deleted")
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )