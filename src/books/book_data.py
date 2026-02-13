from typing import List
from .schemas import Book

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
