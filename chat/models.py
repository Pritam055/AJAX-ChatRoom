from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.CharField(max_length=30)  
    room = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=20)

    