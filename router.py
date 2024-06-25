from fastapi import Depends, APIRouter
from repository import TaskRepository
from schemas import TaskAdd, TaskGet

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("")
async def add_tasks(
        task: TaskAdd = Depends()
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[TaskGet]:
   tasks = await TaskRepository.find_all()
   return tasks

