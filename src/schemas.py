from uuid import UUID

from pydantic import BaseModel


class CreateTaskSchema(BaseModel):
    title: str
    description: str | None = None


class PatchTaskSchema(BaseModel):
    id: UUID
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None
