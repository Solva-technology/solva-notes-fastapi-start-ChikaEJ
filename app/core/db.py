from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, \
    create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, \
    mapped_column

from app.core.config import settings


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


engine = create_async_engine(settings.DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

@asynccontextmanager
async def get_asynq_session():
    async with AsyncSessionLocal() as session:
        yield session
