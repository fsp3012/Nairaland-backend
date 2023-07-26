from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    tags = models.CharField(max_length=15, null=False)
    created_at = models.DateField(auto_now=True)
    story = models.TextField(null=False)
    trending = models.BooleanField(default=False)
