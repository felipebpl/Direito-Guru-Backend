from django.db import models

class Feed(models.Model):
    area = models.CharField(max_length=200)
    duvida = models.TextField()
    data = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.id}. {self.area}'