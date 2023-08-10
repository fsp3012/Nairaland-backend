from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    tags = models.CharField(max_length=100, null=False)
    created_at = models.DateField(auto_now=True)
    story = models.TextField(null=False)
    trending = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='', default='')
    image = CloudinaryField('image', default='')


    class Meta:
         ordering= ['-created_at']
   
    


    
