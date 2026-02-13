from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.reviews.routes import reviews_router
from src.books.routes import books_router
from src.config import Config
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Starting up...")
    await init_db()
    print(Config.DATABASE_URL)
    yield
    print("Finished startup")

app = FastAPI (
    title="Book API", 
    description="A simple API to manage books", 
    version="1.0.0", 
    lifespan=life_span
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
)

@app.get("/", name="Root", tags=["Root"])
async def read_root():
    return {"Healthy": "API is running"}

app.include_router(reviews_router, prefix="/api/v1/reviews")
app.include_router(books_router, prefix="/api/v1/books")

