from src.tasks.models import Tasks
from src.utils.repository import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    """Репозиторий для работы с БД"""

    model = Tasks
