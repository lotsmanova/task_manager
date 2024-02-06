from fastapi import FastAPI
from src.middleware.middleware import logging_middleware
from src.tasks.routers import router as router_task
from src.auth.routers import router as router_user


app = FastAPI(
    title="Task Manager"
)

app.include_router(router_user)
app.include_router(router_task)

app.middleware("http")(logging_middleware)
