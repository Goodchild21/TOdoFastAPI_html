from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


app = FastAPI()
app.mount('/static', StaticFiles(directory='ToDo/static'), 'static')
templates = Jinja2Templates(directory='ToDo/templates')

from ToDo.routes import home #подсвечено не активным, но без него не работает!!!
