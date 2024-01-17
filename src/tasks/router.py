from fastapi import APIRouter
from src.dependies import UOWDep, User_ver
from src.tasks.schemas import TaskAdd, TaskEdit
from src.tasks.tasks_services import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@router.post("")
async def add_task(task: TaskAdd, uow: UOWDep, user: User_ver):
    task_id = await TasksService().add_task(uow, task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks(uow: UOWDep, user: User_ver):
    tasks = await TasksService().get_tasks(uow)
    return tasks


@router.patch("/{id}")
async def edit_task(id: int, task: TaskEdit, uow: UOWDep, user: User_ver):
    await TasksService().edit_task(uow, id, task)
    return {"ok": True}


@router.get("/{id}")
async def get_one_task(id: int, uow: UOWDep, user: User_ver):
    task = await TasksService().get_one_task(uow, id)
    return task


@router.delete("/{id}")
async def delete_task(id: int, uow: UOWDep, user: User_ver):
    await TasksService().delete_task(uow, id)
    return {"message": "task delete"}
