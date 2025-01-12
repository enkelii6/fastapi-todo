from fastapi import Depends, status
from fastapi.responses import Response

from src.dependencies import get_user_id
from src.models import Task
from src.schemas import CreateTaskSchema, PatchTaskSchema


async def list_tasks_handler(user_id: int = Depends(get_user_id)):
    return await Task.filter(user_id=user_id).all()


async def create_task_handler(data: CreateTaskSchema, user_id: int = Depends(get_user_id)):
    await Task.create(user_id=user_id, **data.model_dump())
    return Response(status_code=status.HTTP_201_CREATED)


async def patch_task_handler(data: PatchTaskSchema, user_id: int = Depends(get_user_id)):
    task = await Task.get(id=data.id, user_id=user_id)

    for field, value in data.model_dump().items():
        if value:
            setattr(task, field, value)

    await task.save()
    await task.refresh_from_db()

    return task
