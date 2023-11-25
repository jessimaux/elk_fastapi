import uvicorn
from fastapi import FastAPI
import logging

from logging_setup import LoggerSetup
from routers import home

app = FastAPI()

app.include_router(home.router)

logger_setup = LoggerSetup()
LOGGER = logging.getLogger()

@app.on_event('startup')
async def startup():
    LOGGER.info('startup')


@app.on_event('shutdown')
async def shutdown():
    LOGGER.info('shutdown')


@app.get('/')
def home():
    return 'welcome'
