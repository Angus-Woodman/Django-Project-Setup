from django.db import models

# Create your models here.
from django.db import models
class Breed(models.Model):
    name = models.CharField(max_length=100)
    temperament = models.TextField()

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} the {self.breed.name}'
