from src.tasks.schemas import TaskAdd, TaskEdit
from src.utils.unitofwork import IUnitOfWork


class TasksService:
    """Класс сервиса задач для реализации CRUD"""

    async def add_task(self, uow: IUnitOfWork, task: TaskAdd):
        tasks_dict = task.model_dump()
        async with uow:
            task_id = await uow.tasks.add_one(tasks_dict)
            await uow.commit()
            return task_id

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskEdit):
        tasks_dict = task.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)
            await uow.commit()

    async def delete_task(self, uow: IUnitOfWork, task_id: int):
        async with uow:
            await uow.tasks.delete_one(task_id)
            await uow.commit()

    async def get_one_task(self, uow: IUnitOfWork, task_id: int):
        async with uow:
            task = await uow.tasks.find_one(id=task_id)
            return task
