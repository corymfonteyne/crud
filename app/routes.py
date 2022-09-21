from flask import (
    Flask,
    request
)

app =Flask(__name__)

from app.database import data_types


@app.get("/")
def index():
    out = data_types.scan()
    return out

@app.get("/data_types/integers")
def integers():
    out = data_types.select_by_type(name="Integer")
    return out

@app.get("/data_types/floats")
def integers():
    out = data_types.select_by_type(name="Float")
    return out

@app.get("/data_types/booleans")
def integers():
    out = data_types.select_by_type(name="Boolean")
    return out 

@app.get("/data_types/strings")
def integers():
    out = data_types.select_by_type(name="Strings")
    return out 

@app.get("/data_types/lists")
def integers():
    out = data_types.select_by_type(name="Lists")
    return out 

@app.post("/data_types")
def create_data_type():
    dt_body = request.json
    data_types.create(dt_body)
    return "", 204

@app.put("/data_types/<int:pk>")
def update_data_types(pk):
    dt_body = request.json
    data_types.update(dt_body, pk)
    return "", 204

@app.delete("/data_types/<int:pk>")
def delete_data_type(pk):
    data_types.delete(pk)
    return "", 204