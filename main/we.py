from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    dynco = "Ye"
    return templates.TemplateResponse("are.html", {"request": request, "dynco": dynco})