from sqlmodel import SQLModel, Field, Column, DateTime, text
from uuid import uuid4, UUID
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False, unique=True, )
    title: str = Field(index=True, nullable=False, unique=True, max_length=255)
    author: str
    publisher: str
    page_count: int
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default=datetime.now(),
            server_default=text("CURRENT_TIMESTAMP")
        ))
    updated_at: datetime = Field(
            sa_column=Column(
            pg.TIMESTAMP(timezone=True), 
            server_default=text("CURRENT_TIMESTAMP"), 
            onupdate=pg.TIMESTAMP(timezone=True))
        )
     
    def __repr__(self):
        return f"Created Book: Id={self.id}, Title={self.title}"