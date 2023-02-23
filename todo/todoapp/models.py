from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    discription = models.CharField(max_length=256)
    

    def __str__(self):
        return self.title
