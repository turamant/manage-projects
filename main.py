from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("base clear")
    await create_tables()
    print("Base ready")
    yield
    print("switch off")


app = FastAPI(title="MyProject", lifespan=lifespan)
app.include_router(task_router)

