from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=300)
    time = models.IntegerField()
    person = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index', kwargs={'task_id': self.id})