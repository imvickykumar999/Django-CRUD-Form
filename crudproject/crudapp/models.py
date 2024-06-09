
from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    foto = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
