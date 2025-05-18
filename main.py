from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory= "templates")

connection = MongoClient("mongodb+srv://shubham:HWTlbDGM7YQJjWEg@fastapi-cluster0.4dsvl6p.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    data = connection.airbnb.airbnb.find({}).limit(8)
    # print(data)
    return templates.TemplateResponse("index.html", {"request": request, "hotels": data})

