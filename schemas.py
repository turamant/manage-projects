from pydantic import BaseModel


class TaskAdd(BaseModel):
    name: str
    description: str | None = None


class TaskGet(TaskAdd):
    id: int


