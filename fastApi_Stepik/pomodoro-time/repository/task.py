from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from database import Tasks, Categories
from database import get_db_session, Tasks
from schema.taskschema import TaskSchema


class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self) -> list[Tasks]:  # Возвращаем список задач
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(select(Tasks)).scalars().all()
        return tasks

    def get_task(self, task_id: int) -> Tasks | None:
        with self.db_session() as session:
            task: Tasks = session.execute(
                select(Tasks).where(Tasks.id == task_id)
            ).scalar_one_or_none()
        return task

    def create_task(self, task: TaskSchema) -> int:
        task_model = Tasks(
            name=task.name,
            pomodoro_count=task.pomodoro_count,
            category_id=task.category_id,
        )
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
            return task_model.id

    def delete_task(self, task_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            session.execute(query)
            session.commit()

    def get_task_by_category_name(self, category_name: str) -> list[Tasks]:
        query = (
            select(Tasks)
            .join(Categories, Tasks.category_id == Categories.id)
            .where(Categories.name == category_name)
        )
        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(query).scalars().all()
            return tasks

    def update_task_name(self, task_id: int, name: str) -> TaskSchema:
        query = (
            update(Tasks)
            .where(Tasks.id == task_id)
            .values(name=name)
            .returning(Tasks.id)
        )
        with self.db_session() as session:
            task_id: int = session.execute(query).scalar_one_or_none()
            session.commit()
            return self.get_task(task_id)
