from django.db import models

from django.contrib.auth.models import User

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    day = models.CharField(max_length=10)  # e.g. 'Monday'
    time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} on {self.day} at {self.time}"