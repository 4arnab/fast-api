from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
app = FastAPI(title="Book API", description="A simple API to manage books", version="1.0.0")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: int
    page_count: int
    language: str

class UpdateBookModel(BaseModel):
    title: str  
    author: str
    publisher: str
    page_count: int
    language: str

books:List[Book] = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": 1925,
        "page_count": 218,
        "language"  : "English",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": 1960,
        "page_count": 281,
        "language"  : "English",
    },
]

@app.get("/")
async def read_root():
    return {"Healthy": "API is running"}   

@app.get("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No books found")
    return books

@app.post("/books", status_code = status.HTTP_201_CREATED, response_model=Book)
async def create_book(new_book: Book):
    books.append(new_book)
    return new_book 

@app.get("/books/{book_id}")
async def get_book(book_id:int)-> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:   
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/books/{book_id}")
async def update_book(book_id:int, updated_book: UpdateBookModel) -> UpdateBookModel:
    for book in books:
        print(book['id'], book_id)
        if book['id'] == book_id:
            book['title'] = updated_book.title
            book['author'] = updated_book.author
            book['publisher'] = updated_book.publisher
            book['page_count'] = updated_book.page_count
            book['language'] = updated_book.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")












































































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
