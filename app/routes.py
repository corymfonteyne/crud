from flask import (
    Flask,
    request
)

app =Flask(__name__)


@app.get("/")
def index():
    pass

@app.get("/integers")
def integers():
    out = data_types.select_by_type(_type="init")

@app.get("/floats")
def integers():
    out = data_types.select_by_type(_type="float")

@app.get("/booleans")
def integers():
    out = data_types.select_by_type(_type="bool")