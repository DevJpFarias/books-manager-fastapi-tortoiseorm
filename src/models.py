from tortoise import fields
from tortoise.models import Model

class Book(Model):
  id = fields.IntField(pk=True)
  title = fields.CharField(max_length=255)
  author = fields.CharField(max_length=255)
  published_year = fields.IntField()
  genre = fields.CharField(max_length=50)

  class Meta:
    table = "books"