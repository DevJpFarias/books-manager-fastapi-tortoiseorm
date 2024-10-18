from pydantic import BaseModel

class BookSchema(BaseModel):
  id: int
  title: str
  author: str
  published_year: int
  genre: str

  class Config:
    orm_mode: True

class BookCreateSchema(BaseModel):
  title: str
  author: str
  published_year: int
  genre: str