from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.tasks.models import Tasks, Categories
from app.tasks.schema import TaskSchema


class TaskRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_tasks(self) -> list[TaskSchema]:
        tasks = await self.db_session.execute(select(Tasks))
        tasks = tasks.scalars().all()
        return [TaskSchema.model_validate(task) for task in tasks]

    async def get_task(self, task_id: int) -> Tasks | None:
        result = await self.db_session.execute(
            select(Tasks).where(Tasks.id == task_id)
        )
        return result.scalar_one_or_none()

    async def get_user_task(self, task_id: int, user_id: int) -> Tasks | None:
        query = select(Tasks).where(Tasks.id == task_id, Tasks.user_id == user_id)
        async with self.db_session as session:
            task: Tasks = (await session.execute(query)).scalar_one_or_none()
        return task

    async def create_task(self, task_data: dict) -> Tasks:
        task = Tasks(**task_data)
        self.db_session.add(task)
        await self.db_session.commit()
        await self.db_session.refresh(task)
        return task

    async def delete_task(self, task_id: int, user_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id, Tasks.user_id == user_id)
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def get_task_by_category_name(self, category_name: str) -> list[Tasks]:
        query = (
            select(Tasks)
            .join(Categories, Tasks.category_id == Categories.id)
            .where(Categories.name == category_name)
        )
        async with self.db_session as session:
            task: list[Tasks] = (await session.execute(query)).scalars().all()
            return task

    async def update_task_name(self, task_id: int, name: str) -> Tasks:
        query = (
            update(Tasks)
            .where(Tasks.id == task_id)
            .values(name=name)
            .returning(Tasks.id)
        )
        async with self.db_session as session:
            task_id: int = (await session.execute(query)).scalar_one_or_none()
            await session.commit()
            await session.flush()
            return await self.get_task(task_id)
