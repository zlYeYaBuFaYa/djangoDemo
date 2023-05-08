from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    publish_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "books"


class Hero(models.Model):
    name = models.CharField(max_length=50)
    skill = models.CharField(max_length=100)
    book_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "heroes"
