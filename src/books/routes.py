from fastapi import FastAPI, status, APIRouter
from fastapi.exceptions import HTTPException
from typing import List

from .schemas import Book, UpdateBookModel
from .book_data import Book, books

books_router = APIRouter(tags=["Books"])

@books_router.get("", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No books found")
    return books    

@books_router.post("", status_code = status.HTTP_201_CREATED, response_model=Book)
async def create_book(new_book: Book):
    books.append(new_book)
    return new_book 

@books_router.get("/{book_id}")
async def get_book(book_id:int)-> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@books_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:   
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@books_router.patch("/{book_id}")
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

