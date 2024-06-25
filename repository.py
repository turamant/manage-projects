from sqlalchemy import select
from sqlalchemy.orm import query

from database import new_session, TaskOrm
from schemas import TaskAdd, TaskGet


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[TaskGet]:
        async with new_session() as session:
            query_db = select(TaskOrm)
            result = await session.execute(query_db)
            task_models = result.scalars().all()
            return task_models
