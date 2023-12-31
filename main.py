from fastapi import FastAPI
from typing import Dict, Any
import importlib
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from inspect import getsource, getdoc

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Function:
    def __init__(self, module, name, description, code):
        self.module = module
        self.name = name
        self.description = description
        self.code = code

def dynamic_import(module_name, function_name):
    """Динамически импортирует и возвращает функцию из указанного модуля."""

    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)
    return function

@app.post("/json/")
def process_json(data: Dict[str, Any]) -> Dict[str, Any]:
    """Обрабатывает JSON-запрос, динамически импортирует и выполняет функцию."""  
    
    module_name = data["module"]
    function_name = data["function"]
    function = dynamic_import(module_name, function_name)
    if not function:
        return {"error": f"Unknown function {function_name}"}
    return function(data["data"])

@app.get("/html/", response_class=HTMLResponse)
def show_functions() -> HTMLResponse:
    """Отображает список функций в HTML-формате."""

    modules = ['myname']
    functions = []
    for mod_name in modules:
        module = importlib.import_module(mod_name)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr) and not attr_name.startswith("_"):
                functions.append(Function(mod_name, attr_name, getdoc(attr), getsource(attr)))
    return templates.TemplateResponse("functions.html", {"request": {}, "functions": functions})
