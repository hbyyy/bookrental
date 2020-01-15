from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    description = models.TextField()
    pub_date = models.DateTimeField()


class BookThumbnail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
