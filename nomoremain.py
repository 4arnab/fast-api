from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# importing the books routes
from books.routes import books_router

app = FastAPI(title="Book API", description="A simple API to manage books", version="1.0.0")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(books_router)

@app.get("/")
async def read_root():
    return {"Healthy": "API is running"}   












































































# @app.get("/")
# async  def read_root():
#     return {"Hello": "World"}

# # query parameters and path parameters
# @app.get("/items/{name}")
# async def read_item(name:str, age:Optional[int] = 0) -> dict: # optional query parameters with default values
#     return {"name": f"hello, {name}", "age" : f"your age is {age}"}

# @app.post("/create-book/") # getting data from the request body using Pydantic models
# async def create_item(book_data:BookCreateModel) -> BookCreateModel:
#     return book_data

# @app.get("/get-headers")
# async def get_headers(
#     headers:str = Header(None),
#     host:str = Header(None)
#     ):
#     return {"headers": headers, "host": host}
