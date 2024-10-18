from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from src.models import Book
from src.schemas import BookSchema, BookCreateSchema

app = FastAPI()

register_tortoise(
  app,
  db_url='postgres://docker:docker@localhost:5432/managebooksdb?schema=public',
  modules={'models': ['src.models']},
  generate_schemas=True,
  add_exception_handlers=True
)

@app.post('/books', response_model=BookSchema)
async def create_book(book: BookCreateSchema):
  new_book = await Book.create(**book.model_dump())

  return new_book

@app.get('/books', response_model=list[BookSchema])
async def list_book():
  books = await Book.all()

  return books

@app.put('/books/{book_id}', response_model=BookSchema)
async def update_hook(book_id: int, book: BookCreateSchema):
  existing_book = await Book.get(id=book_id)

  if not existing_book:
    raise HTTPException(status_code=404, detail="Book not found!")
  
  await existing_book.update_from_dict(book.model_dump()).save()

  return existing_book

@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
  book = await Book.get(id=book_id)

  if not book:
    raise HTTPException(status_code=404, detail="Book not found!")
  
  await book.delete()

  return { "message": "Book deleted sucessfully!" }