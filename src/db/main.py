from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine 
from src.config import Config
from src.models.book import Book

engine =AsyncEngine( 
    create_engine(
    url=Config.DATABASE_URL, 
    echo=True,  # Enable SQL query logging
))

async def init_db():
    async with engine.begin() as conn: 
        await conn.run_sync(Book.metadata.create_all)
