from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

web_app = FastAPI()

web_app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@web_app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@web_app.get("/blog")
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

@web_app.get("/blog/reading")
async def reading(request: Request):
    return templates.TemplateResponse("blog/reading.html", {"request": request})

@web_app.get("/blog/the-great-debate")
async def the_great_deabate(request: Request):
    return templates.TemplateResponse("blog/the-great-debate.html", {"request": request})

# @web_app.get("/work")
# async def work(request: Request):
#     return templates.TemplateResponse("work.html", {"request": request})
