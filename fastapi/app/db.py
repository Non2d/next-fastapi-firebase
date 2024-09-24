from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from migrate import async_engine  # migrate.pyからasync_engineをインポート

async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    session = async_session()
    try:
        yield session
    finally:
        await session.close()