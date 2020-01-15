from django.db import models

# Create your models here.


class Rental(models.Model):
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE)
    users = models.ForeignKey('members.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    is_extended = models.BooleanField(default=False)