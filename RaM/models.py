from django.db import models

class Personagem(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name