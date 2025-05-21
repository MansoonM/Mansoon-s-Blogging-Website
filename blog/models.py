from django.db import models
from django.contrib.auth.models import User

class add_blogs(models.Model):
    name=models.CharField(max_length=40)
    add_blog=models.CharField(max_length=1000)
    checking=models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title


class add_thought(models.Model):
    name=models.CharField(max_length=50)
    thought=models.CharField(250)
    checking=models.BooleanField(default=False)


class contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    number=models.CharField(max_length=10)
    feedback=models.CharField(max_length=200)

    # def __str__(self):
    #     return self.title
