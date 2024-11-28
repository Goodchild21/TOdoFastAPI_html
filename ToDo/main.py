from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


app = FastAPI()
app.mount('/static', StaticFiles(directory='todo/static'), 'static')
templates = Jinja2Templates(directory='todo/templates')

from todo.routes import home #подсвечено не активным, но без него не работает!!!