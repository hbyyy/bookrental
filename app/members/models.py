from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models


class User(AbstractUser):
    rate_date = models.DateTimeField(null=True)
