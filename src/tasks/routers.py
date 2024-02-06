from typing import Set
from fastapi import APIRouter, HTTPException, status, Depends
from starlette.websockets import WebSocket, WebSocketDisconnect

from src.auth.jwt import get_user_by_token
from src.dependies import UOWDep
from src.tasks.schemas import TaskAdd, TaskEdit
from src.tasks.services import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)

active_connections: Set[WebSocket] = set()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(client_id: int, websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            for connection in active_connections:
                await connection.send_text(f"Client with {client_id} wrote {message}!")
    except WebSocketDisconnect:
        active_connections.remove(websocket)


@router.post("")
async def add_task(task: TaskAdd, uow: UOWDep, username: str = Depends(get_user_by_token)):
    try:
        task_id = await TasksService().add_task(uow, task)
        for connection in active_connections:
            await connection.send_text(f"New task created: {task.title}")
        return {"task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("")
async def get_tasks(uow: UOWDep):
    try:
        tasks = await TasksService().get_tasks(uow)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.patch("/{id}")
async def edit_task(id: int, task: TaskEdit, uow: UOWDep, username: str = Depends(get_user_by_token)):
    try:
        await TasksService().edit_task(uow, id, task)
        for connection in active_connections:
            await connection.send_text(f"Task {task.title} updated")
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{id}")
async def get_one_task(id: int, uow: UOWDep, username: str = Depends(get_user_by_token)):
    try:
        task = await TasksService().get_one_task(uow, id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/{id}")
async def delete_task(id: int, uow: UOWDep, username: str = Depends(get_user_by_token)):
    try:
        task = await TasksService().get_one_task(uow, id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        await TasksService().delete_task(uow, id)
        for connection in active_connections:
            await connection.send_text(f"Task {id} deleted")
        return {"message": "task deleted"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
