from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Response, status
from tortoise import Tortoise

from src.config import TORTOISE_CONFIG
from src.handlers import create_task_handler, list_tasks_handler, patch_task_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_CONFIG)
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)


@app.get('/health/')
async def health():
    return Response(status_code=status.HTTP_200_OK)


app.add_api_route('/', list_tasks_handler)
app.add_api_route('/', create_task_handler, methods=['POST'])
app.add_api_route('/', patch_task_handler, methods=['PATCH'])


if __name__ == '__main__':
    uvicorn.run('src.app:app', host='0.0.0.0', port=8000, reload=True)
