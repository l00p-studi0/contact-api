from django.db import models


# Create your models here.
class User(models.Model):
    Fullname = models.CharField(max_length = 50)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Comment = models.TextField()

class Meta:
    db_table = "User"