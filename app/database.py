from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
DATABASE_URL = "postgresql+asyncpg://postgres:admin123@localhost:5432/ecommerce_db"
engine = create_async_engine(DATABASE_URL, pool_size=20, max_overflow=10)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield AsyncSession
        finally:
            await session.close()