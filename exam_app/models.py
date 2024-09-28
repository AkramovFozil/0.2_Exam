from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()

