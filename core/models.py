from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=250)
    director = models.CharField(max_length=100)
    trailer = models.FileField(upload_to='trailer' , blank=True , null = True)
    cover = models.ImageField(upload_to='covers' , null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} by {self.director}"
