from starlette.staticfiles import StaticFiles

from config import DB_URL, DBPaths
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

from db.users.endpoints import user_router
from db.project.endpoints import router as project_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Coldy',
    description="API",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://127.0.0.1:8080',
        'http://127.0.0.1:8000'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_router, prefix="/users", tags=["Пользователи"])

app.include_router(project_router, prefix="/projects", tags=["Проекты"])

app.mount("/static", StaticFiles(directory="static"), name="static")

register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": DBPaths.all_paths},
    generate_schemas=True,
    add_exception_handlers=True,
)
